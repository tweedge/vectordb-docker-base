# vectordb-docker-base

Python 3.10-slim with [VectorDB](https://github.com/kagisearch/vectordb) (`vectordb2==0.1.9`). amd64 only at this time.

This image is intended for use as a base image to build other applications on top of, so any independent application that needs VectorDB (and whoof I have a number of usecases here) can pull one set of enormous prebuilt layers and then only add minor layers on top for each application/deployment.

### Tagged Images

Tagged images, sorted by size (smallest to largest):
* `core` - just vectordb2, use this if you will download your own model during build, which you can do automatically by running `python3 /opt/dependencies/initialize.py <HuggingFace model name>` ex. `python3 /opt/dependencies/initialize.py TaylorAI/bge-micro-v2`
* `bge-small-en-v1.5` - imported [BAAI/bge-small-en-v1.5](https://huggingface.co/BAAI/bge-small-en-v1.5)) (+0.13GB, 384 dimensions, 512 sequence length)
* `bge-base-en-v1.5` - imported [BAAI/bge-base-en-v1.5](https://huggingface.co/BAAI/bge-base-en-v1.5)) (+0.44GB, 768 dimensions, 512 sequence length)
* `bge-large-en-v1.5` - imported [BAAI/bge-large-en-v1.5](https://huggingface.co/BAAI/bge-large-en-v1.5)), (+1.34GB, 1024 dimensions, 512 sequence length)

For detailed performance comparisons, check out [MTEB](https://huggingface.co/spaces/mteb/leaderboard).

### Notes/Maintenance

I recommend making your own copy of this repo if you want to fine tune any performance characteristics.

This is for my personal projects and is not guaranteed to be stable.

Just clone the repo and run your own, it's all auto-built anyway and fits well within the GitHub free plan.