FROM python:3.10-slim
LABEL maintainer="Chris Partridge <chris@partridge.tech>"

RUN mkdir /opt/dependencies/

COPY ./dependencies/. /opt/dependencies/

RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    apt-get purge -y --auto-remove && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache -r /opt/dependencies/requirements.txt && \
    python3 /opt/dependencies/initialize.py