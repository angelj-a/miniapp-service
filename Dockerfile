FROM python:3.5.0-slim

COPY bashrc /root/.bashrc

COPY sources.list /etc/apt/sources.list
COPY build-dependencies.txt /tmp/
RUN apt-get update && apt-get install $(cat /tmp/build-dependencies.txt | awk '{print $1}') -y

COPY py-requirements.txt /tmp/
RUN pip install --upgrade pip && pip install -r /tmp/py-requirements.txt