FROM python:slim

RUN \
    apt-get update -y && \
    apt-get install -y \
        curl \
        git

COPY requirements.txt requirements.txt

RUN \
    pip install -r requirements.txt

WORKDIR /app
