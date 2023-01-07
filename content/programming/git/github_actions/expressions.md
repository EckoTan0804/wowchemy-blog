---
# ===== Title, summary, and position in the left sidebar =====
linktitle:  # Title shown in the left sidebar menu
summary:  # Summary of this post
weight: 304
# ============================================================

# ========== Basic metadata ==========
title: Expressions
date: 2023-01-06
draft: false
type: book # page type
authors:
  - admin
tags:
  - Coding
  - Git
  - GitHub
  - GitHub Actions
categories:
  - Coding
toc: true # Show table of contents
# ====================================

# ========== Advanced metadata =========
profile: false  # Show author profile?
reading_time: true # Show estimated reading time?
share: true  # Show social sharing links?
featured: true
comments: true  # Show comments?
disable_comment: false
commentable: true  # Allow visitors to comment? Supported by the Page, Post, and Book content types.
editable: false  # Allow visitors to edit the page? Supported by the Page, Post, and Book content types.

# Optional header image (relative to `assets/media/` folder).
header:
  caption: 
  image:  
---

## Overview

You can use expressions to *programmatically* set environment variables in workflow files and access contexts. An expression can be any combination of literal values, references to a context, or functions. You can combine literals, context references, and functions using operators.

Expressions are commonly used with the conditional `if` keyword in a workflow file to determine whether a step should run. When an `if` conditional is `true`, the step will run.

You need to use specific syntax 

```yaml
${{ <expression> }}
```

to tell GitHub to evaluate an expression rather than treat it as a string.

- When you use expressions in an `if` conditional, you may omit the expression syntax (`${{ }}`) because GitHub automatically evaluates the `if` conditional as an expression. 

#### Example expression in an `if` conditional

```yaml
steps:
  - uses: actions/hello-world-javascript-action@v1.1
    if: ${{ <expression> }}
```

#### Example setting an environment variable

```yaml
env:
  MY_ENV_VAR: ${{ <expression> }}
```

## Literals

You can use `boolean`, `null`, `number`, or `string` data types.

| Data type | Literal value                                                |
| :-------- | :----------------------------------------------------------- |
| `boolean` | `true` or `false`                                            |
| `null`    | `null`                                                       |
| `number`  | Any number format supported by JSON.                         |
| `string`  | You don't need to enclose strings in `${{` and `}}`. However, if you do, you must use single quotes (`'`) around the string. To use a literal single quote, escape the literal single quote using an additional single quote (`''`). Wrapping with double quotes (`"`) will throw an error. |

Example:

```yaml
env:
  myNull: ${{ null }}
  myBoolean: ${{ false }}
  myIntegerNumber: ${{ 711 }}
  myFloatNumber: ${{ -9.2 }}
  myHexNumber: ${{ 0xff }}
  myExponentialNumber: ${{ -2.99e-2 }}
  myString: Mona the Octocat
  myStringInBraces: ${{ 'It''s open source!' }}
```

## Operators

| Operator | Description           |
| :------- | :-------------------- |
| `( )`    | Logical grouping      |
| `[ ]`    | Index                 |
| `.`      | Property de-reference |
| `!`      | Not                   |
| `<`      | Less than             |
| `<=`     | Less than or equal    |
| `>`      | Greater than          |
| `>=`     | Greater than or equal |
| `==`     | Equal                 |
| `!=`     | Not equal             |
| `&&`     | And                   |
| `||`     | Or                    |

GitHub performs loose equality comparisons.

- If the types do not match, GitHub coerces the type to a number. GitHub casts data types to a number using these conversions:

  | Type    | Result                                                       |
  | :------ | :----------------------------------------------------------- |
  | Null    | `0`                                                          |
  | Boolean | `true` returns `1` `false` returns `0`                       |
  | String  | Parsed from any legal JSON number format, otherwise `NaN`. Note: empty string returns `0`. |
  | Array   | `NaN`                                                        |
  | Object  | `NaN`                                                        |

- A comparison of one `NaN` to another `NaN` does not result in `true`. 

- GitHub ignores case when comparing strings.

- Objects and arrays are only considered equal when they are the *same instance*.

## Functions

- GitHub offers a set of built-in functions that you can use in expressions.

- Some functions cast values to a string to perform comparisons. GitHub casts data types to a string using these conversions:

  | Type    | Result                                        |
  | :------ | :-------------------------------------------- |
  | Null    | `''`                                          |
  | Boolean | `'true'` or `'false'`                         |
  | Number  | Decimal format, exponential for large numbers |
  | Array   | Arrays are not converted to a string          |
  | Object  | Objects are not converted to a string         |

### conatins

`contains( search, item )`

- Returns `true` if `search` contains `item`. 
- If `search` is an array, this function returns `true` if the `item` is an element in the array. 
- If `search` is a string, this function returns `true` if the `item` is a substring of `search`. This function is not case sensitive. Casts values to a string.

#### Example

`contains('Hello world', 'llo')` returns `true`.

### startsWith

`startsWith( searchString, searchValue )`

Returns `true` when `searchString` starts with `searchValue`. This function is not case sensitive. Casts values to a string.

#### Example

`startsWith('Hello world', 'He')` returns `true`.

### endsWith

`endsWith( searchString, searchValue )`

Returns `true` if `searchString` ends with `searchValue`. This function is not case sensitive. Casts values to a string.

#### Example

`endsWith('Hello world', 'ld')` returns `true`.

### format

`format( string, replaceValue0, replaceValue1, ..., replaceValueN)`

- Replaces values in the `string`, with the variable `replaceValueN`. 
- Variables in the `string` are specified using the `{N}` syntax, where `N` is an integer. You must specify at least one `replaceValue` and `string`. There is no maximum for the number of variables (`replaceValueN`) you can use. 
- Escape curly braces using double braces.

#### Example

`format('{{Hello {0} {1} {2}!}}', 'Mona', 'the', 'Octocat')` returns '{Hello Mona the Octocat!}'.

### join

`join( array, optionalSeparator )`

- The value for `array` can be an array or a string. 
- All values in `array` are concatenated into a string. 
  - If you provide `optionalSeparator`, it is inserted between the concatenated values. Otherwise, the default separator `,` is used. Casts values to a string.

### toJSON

`toJSON(value)`

- Returns a pretty-print JSON representation of `value`. 
- You can use this function to debug the information provided in contexts.

### fromJSON

`fromJSON(value)`

- Returns a JSON object or JSON data type for `value`. 
- You can use this function to provide a JSON object as an evaluated expression or to convert environment variables from a string.

### hashFiles

`hashFiles(path)`

- Returns a single hash for the set of files that matches the `path` pattern. 
  - You can provide a single `path` pattern or multiple `path` patterns separated by commas. 
  - The `path` is relative to the `GITHUB_WORKSPACE` directory and can only include files inside of the `GITHUB_WORKSPACE`. 
- This function calculates an individual SHA-256 hash for each matched file, and then uses those hashes to calculate a final SHA-256 hash for the set of files. 
  - If the `path` pattern does not match any files, this returns an empty string.

## Status Check Functions

You can use the following status check functions as expressions in `if` conditionals. A default status check of `success()` is applied unless you include one of these functions.

### success

Returns `true` when none of the previous steps have failed or been canceled.

#### Example

```yaml
steps:
  ...
  - name: The job has succeeded
    if: ${{ success() }}
```

### always

Causes the step to always execute, and returns `true`, even when canceled. A job or step will not run when a critical failure prevents the task from running. For example, if getting sources failed.

#### Example

```yaml
if: ${{ always() }}
```

### cancelled

Returns `true` if the workflow was canceled.

#### Example

```yaml
if: ${{ cancelled() }}
```

### failure

Returns `true` when any previous step of a job fails. If you have a chain of dependent jobs, `failure()` returns `true` if any ancestor job fails.

#### Example

```yaml
steps:
  ...
  - name: The job has failed
    if: ${{ failure() }}
```

#### ailure with conditions

You can include extra conditions for a step to run after a failure, but you must still include `failure()` to override the default status check of `success()` that is automatically applied to `if` conditions that don't contain a status check function.

##### Example

```yaml
steps:
  ...
  - name: Failing step
    id: demo
    run: exit 1
  - name: The demo step has failed
    if: ${{ failure() && steps.demo.conclusion == 'failure' }}
```

## Object filters

You can use the `*` syntax to apply a filter and select matching items in a collection.

E.g., let's say we have an array of objects named `fruits`:

```json
[
  { "name": "apple", "quantity": 1 },
  { "name": "orange", "quantity": 2 },
  { "name": "pear", "quantity": 1 }
]
```

The filter `fruits.*.name` returns the array `[ "apple", "orange", "pear" ]`.

You may also use the `*` syntax on an object. For example, suppose you have an object named `vegetables`:

```json
{
  "scallions":
  {
    "colors": ["green", "white", "red"],
    "ediblePortions": ["roots", "stalks"],
  },
  "beets":
  {
    "colors": ["purple", "red", "gold", "white", "pink"],
    "ediblePortions": ["roots", "stems", "leaves"],
  },
  "artichokes":
  {
    "colors": ["green", "purple", "red", "black"],
    "ediblePortions": ["hearts", "stems", "leaves"],
  },
}
```

The filter `vegetables.*.ediblePortions` could evaluate to:

```json
[
  ["roots", "stalks"],
  ["hearts", "stems", "leaves"],
  ["roots", "stems", "leaves"],
]
```

Since objects don't preserve order, the order of the output can not be guaranteed.

## Reference

- [Expressions](https://docs.github.com/en/actions/learn-github-actions/expressions#object-filters)