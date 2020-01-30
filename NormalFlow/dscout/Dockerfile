FROM ubuntu:bionic

RUN apt update && apt install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install pika
COPY oper.py /app/oper.py
RUN chmod u+x /app/oper.py
CMD /app/oper.py
