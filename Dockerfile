FROM python:3.6.2
ENV PYTHONUNBUFFERED 1
RUN mkdir /docker_container

WORKDIR /docker_container
ADD . /docker_container/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /docker_container/
RUN apt-get update
