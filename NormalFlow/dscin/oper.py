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

#setup excahnges

channel.exchange_declare(exchange='traces', exchange_type='direct')
channel.exchange_declare(exchange='historyheader', exchange_type='topic')

# check if queue exist. else create
outqueue = channel.queue_declare(queue='DSCIN',auto_delete=True)
outhhqueue= channel.queue_declare(queue='HHDSCIN',auto_delete=True)

# bind a queue to an exchange
channel.queue_bind(exchange='traces',
                   queue=outqueue.method.queue)
channel.queue_bind(exchange='historyheader',
                   queue=outhhqueue.method.queue,
                   routing_key="DSCIN.historyheader")

############### preperation phase
print("sending historyheader", flush=True)
history_header={
    "VERSION": 1.0
}
channel.basic_publish(exchange='historyheader', 
                    routing_key='DSCIN.historyheader', 
                    body=json.dumps(history_header),
)

############### execution phase
trace={
    "VERSION": 1.0,
    "TRACEHEADER": {
        "SSP": "hello",
        "POS": 1,
        "SEQ": 0
    },
    "TRACEDATA": [
        1.233,
        1.234,
        1.234,
    ]   
}

# push a message to rabbitmq
for i in range(0,100):
    print("sending trace",i, flush=True)
    trace["TRACEHEADER"]["SEQ"]=i
    channel.basic_publish(exchange='traces', routing_key='DSCIN', body=json.dumps(trace))

# send end of data 
channel.basic_publish(exchange='traces', routing_key='DSCIN', body=json.dumps({"END":True}))

# close connection
connection.close()
