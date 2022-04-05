---
linktitle: ''
summary: ''
weight: 13
title: Image
date: 2020-12-13
draft: false
type: book
authors:
- admin
tags:
- Docker
- getting-started
categories:
- Coding
toc: true
profile: false
reading_time: true
share: true
featured: true
comments: true
disable_comment: false
commentable: true
editable: false
header:
  caption: ''
  image: ''
---

## TL;DR

**Lifecycle**

- [`docker images`](https://docs.docker.com/engine/reference/commandline/images) shows all images.
- [`docker import`](https://docs.docker.com/engine/reference/commandline/import) creates an image from a tarball.
- [`docker build`](https://docs.docker.com/engine/reference/commandline/build) creates image from Dockerfile.
- [`docker commit`](https://docs.docker.com/engine/reference/commandline/commit) creates image from a container, pausing it temporarily if it is running.
- [`docker rmi`](https://docs.docker.com/engine/reference/commandline/rmi) removes an image.
- [`docker load`](https://docs.docker.com/engine/reference/commandline/load) loads an image from a tar archive as STDIN, including images and tags (as of 0.7).
- [`docker save`](https://docs.docker.com/engine/reference/commandline/save) saves an image to a tar archive stream to STDOUT with all parent layers, tags & versions (as of 0.7).

**Info**

- [`docker history`](https://docs.docker.com/engine/reference/commandline/history) shows history of image.
- [`docker tag`](https://docs.docker.com/engine/reference/commandline/tag) tags an image to a name (local or registry).

**Cleaning up**

- `docker image prune` is also available for removing unused images. (See [Prune](https://github.com/wsargent/docker-cheat-sheet#prune)).

## Basic usages

In Docker, everything is based on Images. Images are **templates** for creating docker containers.

### Listing images

```bash
docker images
```

```
REPOSITORY               TAG          IMAGE ID       CREATED         SIZE
docker-hello-world_web   latest       85f9e3024e99   14 hours ago    196MB
my_image                 0.0.1        9f3378bbf7e4   36 hours ago    133MB
nginx                    v3           6ed4b5e97df7   37 hours ago    133MB
python                   3.7-alpine   0ce5215b0b31   43 hours ago    41.1MB
nginx                    latest       7baf28ea91eb   2 days ago      133MB
ubuntu                   latest       f643c72bc252   2 weeks ago     72.9MB
```

- `REPOSITORY` : repository source of image

- `TAG` : tag of image

  - There could be a number of tags in the same repository source, representing different version of this repository source. For example, in `ubuntu` repository source, there are many different versions such as 15.10, 14.04, etc. We use `REPOSITORY:TAG` to specify different images

  - For example, if we want to run container with `ubuntu` version 15.10:

    ```bash
    docker run -t -i ubuntu:15.10 /bin/bash
    ```

- `IMAGE ID` : ID of image

- `CREATED`: creation time of image
- `SIZE` : size of image

### Downloading images

Docker automatically downloads a non-existent image when we use it on the local host. If we want to pre-download the image, we can use the `docker pull` command to download it.

For example, we download `ubuntu:13.10`, which doesn't exist in the local machine:

```bash
docker pull ubuntu:13.10
```

### Searching images

We can search images in [Docker Hub](https://hub.docker.com/).

### Removing images

Removing image using image ID:

```bash
docker rmi <image-ID>
```

Removing image using image name

```bash
docker rmi <image-name>
```

### Building image

We use the command `docker build` to create a new image from scratch. To do this, we need to create a `Dockerfile` file that contains a set of instructions to tell Docker how to build our image. (More see [Dockerfile]({{< relref "learn-dockerfile.md" >}}))

### Tagging image

```
docker tag <image-ID> <image-tag>
```

## Reference

- [Docker 镜像使用](https://www.runoob.com/docker/docker-image-usage.html)

- [Docker - Images](https://www.tutorialspoint.com/docker/docker_images.htm)

- [wsargent](https://github.com/wsargent)/**[docker-cheat-sheet](https://github.com/wsargent/docker-cheat-sheet)**