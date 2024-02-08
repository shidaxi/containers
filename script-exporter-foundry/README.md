## build manually

```shell
docker build -t script-exporter-foundry:manually . -f Dockerfile.alpine --build-arg BASE=python:3.10.13-alpine --build-arg VERSION=v2.17.0
docker run --rm -it script-exporter-foundry:manually sh

docker build -t script-exporter-foundry:manually . -f Dockerfile.debian --build-arg BASE=python:3.10.13-bullseye --build-arg VERSION=v2.17.0
docker run --rm -it script-exporter-foundry:manually sh
```