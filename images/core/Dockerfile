FROM python:3.10-slim
LABEL maintainer="Chris Partridge <chris@partridge.tech>"

ENV PYTHONUNBUFFERED 1

RUN mkdir /opt/dependencies/

COPY ./dependencies/. /opt/dependencies/

RUN pip3 install --no-cache -r /opt/dependencies/requirements.txt