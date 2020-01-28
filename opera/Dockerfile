FROM ubuntu:bionic

RUN apt update && apt install -y \
    git \
    cmake \
    openssl-dev \
    && rm -rf /var/lib/apt/lists/*

RUN git clone -b 'v0.10.0' https://github.com/alanxz/rabbitmq-c.git /rabbitmq-c

WORKDIR /rabbitmq-c
RUN mkdir build && cd build && cmake .. && cmake --build . --target install