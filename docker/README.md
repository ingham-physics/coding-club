
# Coding Club Docker

17/05/2021 - Phillip Chlap

## Introduction to Docker

- [Docker Overview](https://docs.docker.com/get-started/overview/)
- [Docker Tutorial for Beginners (Video)](https://www.youtube.com/watch?v=fqMOX6JJhGo&ab_channel=freeCodeCamp.org)
- [Docker Mastery (Udemy)](https://www.udemy.com/course/docker-mastery)
- [DockerCon](https://www.docker.com/dockercon-live/2021/)

## Pulling and Running Images

- [DockerHub](https://hub.docker.com/search?q=&type=image)

### Pull an image

```bash
docker pull ubuntu:20.04
```

### Run a container

```bash
docker run --name mycontainer ubuntu:20.04
```

- `--name`: give your container a name so that you can easily refer to it later

### Run a container (and attach to shell)

```bash
docker run -it --rm ubuntu:20.04 /bin/bash
```

- `-it`: Run this command interactively so that we can use the shell
- `--rm`: Remove this container as soon as it exits

### Check running containers

```bash
docker ps -a
```

- `-a`: Show all containers (even those which have exited)

### Remove old containers

```bash
docker rm mycontainer
```

## Build our own Docker Image

### Define a Dockerfile

```dockerfile
FROM ubuntu:20.04

RUN apt-get update; apt-get install -y python3 python3-pip git

RUN ln -s /usr/bin/python3 /usr/bin/python

COPY example/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY example/app.py /app.py

EXPOSE 8050

ENTRYPOINT  ["tail", "-f", "/dev/null"]
```

### Build the Docker image

```bash
docker build -t myimage .
```

- `-t myimage`: Tags the image
- `.`: Builds the Dockerfile found in the current directory (`cd` into the directory containing the Dockerfile)

### Run a container using our new Docker image

```bash
docker run -d --rm -p 80:8050 --name myapp myimage
```

- `-d`: Detach to allow running this in the background
- `--rm`: Remove this container as soon as it exits
- `-p 80:8050`: Connect port 80 on our machine (the host) to port 8050 in the container
- `--name`: give your container a name so that you can easily refer to it later

## Setting up VSCode Dev Container

- [Developing inside a Container](https://code.visualstudio.com/docs/remote/containers)
- [Remote Development Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)

### Specify Dev Container configuration in .devcontainer.json

```json
{
    "name": "Coding Club Development",
    "dockerFile": "docker/Dockerfile",
    "workspaceFolder": "/code",
    "workspaceMount": "source=${localWorkspaceFolder},target=/code,type=bind,consistency=cached",
    "appPort": [
        8050
    ],
    // Add the IDs of extensions you want installed when the container is created in the array below.
    "extensions": [
        "ms-python.python",
        "njpwerner.autodocstring",
        "eamodio.gitlens"
    ]
}
```

## Deploy on WWW

- [Google Cloud Platform](https://cloud.google.com/run)
- [Amazon Web Services](https://aws.amazon.com/getting-started/hands-on/deploy-docker-containers/)
- [Azure](https://docs.microsoft.com/en-us/learn/modules/run-docker-with-azure-container-instances/)
- [Heroku](https://devcenter.heroku.com/articles/container-registry-and-runtime)
- Or anywhere else where you can run containers!

### Replace `ENTRYPOINT` with `CMD` to run gunicorn server

```dockerfile
CMD gunicorn app:server -b :$PORT
```

### Example for Heroku (for app named ingham-docker-demo)

```bash
heroku login

heroku container:login

heroku container:push -a ingham-docker-demo web

heroku container:release -a ingham-docker-demo web
```

## More Docker

This is only a tiny portion of what can be done with Docker. Explore more features like:

- [Docker Compose](https://docs.docker.com/compose/gettingstarted/)
- [Docker Volumes](https://docs.docker.com/storage/volumes/)
- [Docker Networking](https://docs.docker.com/network/)
- [Share on DockerHub](https://docs.docker.com/docker-hub/)
- And much much more...
