# vectordb-docker-base

Python 3.10-slim with [VectorDB](https://github.com/kagisearch/vectordb) (`vectordb2==0.1.9`). amd64 only at this time. Probably make your own if you want to fine tune any performance characteristics. This is for my personal projects and is not guaranteed to be stable. Seriously, just clone the repo and run your own, it's all auto-built anyway ...

This image is intended for use as a base image to build other applications on top of, so any independent application that needs VectorDB (and whoof I have a number of usecases here) can pull one set of enormous layers and then only add minor layers on top for each application/deployment.

Tagged images:
* `core` - just vectordb2, use this if you will download your own model during build
* `bge-small-en-v1.5` - vectordb2 + the default model ([details](https://huggingface.co/BAAI/bge-small-en-v1.5))
* `bge-base-en-v1.5` - vectordb2 + a "better" (read: higher dimensionality) default model suggested for use ([details](https://huggingface.co/BAAI/bge-base-en-v1.5))