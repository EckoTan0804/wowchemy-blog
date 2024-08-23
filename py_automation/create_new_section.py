import argparse
import yaml

from datetime import datetime
from pathlib import Path
from pprint import pprint as print

import create_index_fontmatter as fontmatter_creater


class MenuItem(object):
    def __init__(self, name, identifier, weight, dir_name, parent=None):
        self.name = name
        self.identifier = identifier
        self.weight = weight
        self.dir_name = dir_name
        self.url = f"{self.parent.url}/{self.dir_name}/" if parent else f"{self.dir_name}"


def name2identifier(name):
    # Example
    # "PyTorch" -> "pytorch"
    # "Computer Vision" -> "computer vision"
    word_list = name.split(" ")
    assert len(word_list) >= 1

    if len(word_list) == 1:
        identifier = name.lower()
    elif len(word_list) > 1:
        word_list = [word.lower() for word in word_list]
        identifier = "-".join(word_list)

    return identifier


def get_menu_item(identifier, menu_item_list):
    menu_item_list = [menu_item for menu_item in menu_item_list if menu_item["identifier"] == identifier]
    assert len(menu_item_list) <= 1  # Identifier should be unique or does not exist

    return None if len(menu_item_list) == 0 else menu_item_list[0]


def is_menu_item_exist(identifier, menu_item_list):
    return True if get_menu_item(identifier, menu_item_list) else False


def sort_menu_item_list(menu_item_list, reverse=False):
    # Sort menu item list based on weight
    menu_item_list.sort(key=lambda x: x["weight"], reverse=reverse)


def get_child_menu_items(parent_identifier, menu_item_list):
    assert is_menu_item_exist(parent_identifier, menu_item_list)
    child_item_list = [menu_item for menu_item in menu_item_list if menu_item.get("parent") == parent_identifier]

    return child_item_list


def suggest_weight(parent_identifier, menu_item_list):
    if not parent_identifier:  # Top-level menu item
        max_weight = menu_item_list[-1]["weight"]
        weight = (max_weight // 100 + 1) * 100
    else:  # Sub-level menu item
        child_menu_item_list = get_child_menu_items(parent_identifier, menu_item_list)
        sort_menu_item_list(child_menu_item_list)
        max_child_weight = child_menu_item_list[-1]["weight"]
        weight = max_child_weight + 1

    return weight


def parse_args():
    parser = argparse.ArgumentParser(description="Automatically create a new section.")

    parser.add_argument(
        "-n",
        "--name",
        type=str,
        required=True,
        help="Name of the section.",
    )

    parser.add_argument(
        "-i",
        "--identifier",
        type=str,
        default=None,
        help="Identifier of the section.",
    )

    parser.add_argument(
        "-p",
        "--parent",
        type=str,
        default=None,
        help="Identifier of parent of the section.",
    )

    return parser.parse_args()


if __name__ == "__main__":
    ROOT_DIR = Path(__file__).parent.parent
    CONTENT_DIR = ROOT_DIR.joinpath("content")

    # Read current config/_default/menus.yaml
    menu_yaml = ROOT_DIR.joinpath("config", "_default", "menus.yaml")
    assert menu_yaml.exists()

    with open(menu_yaml, "r") as f:
        menu_item_dict = yaml.safe_load(f)

    menu_item_list = menu_item_dict["main"]
    sort_menu_item_list(menu_item_list)
    # print(menu_item_list)

    args = parse_args()

    sec_name = args.name
    if not args.identifier:
        sec_identifier = name2identifier(sec_name)

    if args.parent:
        sec_parent = args.parent
        assert is_menu_item_exist(sec_parent, menu_item_list), f"Specified parent of {sec_parent} does not exist!"

    sec_url = f"{args.parent}/{sec_identifier}" if args.parent else sec_identifier

    sec_weight = suggest_weight(sec_parent, menu_item_list)

    # Initialize correponding directory
    sec_dir = ROOT_DIR.joinpath("content", sec_url)
    sec_dir.mkdir(exist_ok=True)
    print(f"Create {str(sec_dir)}")

    # Write _index.md
    if args.parent:
        current_date = datetime.now().strftime("%Y-%m-%d")  # Get current date in YYYY-mm-dd format
        index_fontmatter = fontmatter_creater.create_sub_level_index_fontmatter(
            sec_name,
            current_date,
            sec_weight % 100,
            sec_identifier,
            sec_parent,
        )
    else:
        index_fontmatter = fontmatter_creater.create_top_level_index_fontmatter(sec_name)

    sec_dir_index_file = sec_dir.joinpath("_index.md")
    with open(sec_dir_index_file, "w") as writer:
        writer.write(index_fontmatter)

    print(f"Write fontmatter in {str(sec_dir_index_file)}")

    # Create menu item for new section
    sec_menu_item = {
        "name": sec_name,
        "url": sec_url,
        "identifier": sec_identifier,
        "parent": sec_parent,
        "weight": sec_weight,
    }

    if not sec_parent:
        del sec_menu_item["parent"]

    # Update menu item list
    menu_item_list.append(sec_menu_item)
    sort_menu_item_list(menu_item_list)
    menu_item_dict.update({"main": menu_item_list})

    # Write dict to config/_default/menus.yaml
    with open(menu_yaml, "w") as f:
        yaml.safe_dump(menu_item_dict, f, default_flow_style=False, sort_keys=False, indent=2)

    print(f"Update {str(menu_yaml)}")
