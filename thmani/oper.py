#!/usr/bin/python3
import pika
import json
import time

# connect to rabbitmq message server
credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters(host='rabbitmq',port=5672,credentials=credentials,connection_attempts=5,retry_delay=5)
connection = None
try:
    connection = pika.BlockingConnection(parameters)
except Exception as e:
    print(e,flush=True)

# setup channel
channel = connection.channel()

# check if queue exist. else create
channel.queue_declare(queue='hello')

trace={
    VERSION: 1.0,
    TRACEHEADER: {
        SSP: "hello",
        POS: 1,
        SEQ: 0
    },
    TRACEDATA: [
        1.233,
        1.234,
        1.234,
    ]   
}

# initialization phase

# execution phase
for i in range(0,100):
    trace[TRACEHEADER][SEQ]=i
    channel.basic_publish(exchange='test', routing_key='test', body=json.dumps(trace))
    time.sleep(1)

# finalization phase
connection.close()
