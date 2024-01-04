# vectordb-docker-base

Python 3.10-slim with [VectorDB](https://github.com/kagisearch/vectordb) (`vectordb2==0.1.9`) and the default embedding model ([BAAI/bge-small-en-v1.5](https://huggingface.co/BAAI/bge-small-en-v1.5)) initialized. amd64 only at this time. Probably make your own if you want to fine tune any performance characteristics.

Intended for use as a base image to build other applications on top of, so any independent application that needs VectorDB (and whoof I have a number of usecases here) can pull one set of enormous layers and then only add minor layers on top for each application/deployment.