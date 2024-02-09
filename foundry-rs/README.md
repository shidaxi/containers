## build manually

```shell
docker build -t foundry-rs:manually . -f Dockerfile.alpine --build-arg BASE=alpine:3.19 --build-arg VERSION=2024-01-09
docker run --rm -it foundry-rs:manually sh
```