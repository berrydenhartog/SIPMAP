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
channel.queue_declare(queue='DSCIN')
channel.queue_declare(queue='THMANI')

# get traces
for method_frame, properties, body in channel.consume('DSCIN'):

    #Receive trace from DSCIN
    mytrace = json.loads(body)
    print("THMANI" + json.dumps(mytrace), flush=True)

    # call fortran operation    

    # Send trace to next operation
    channel.basic_publish(exchange='', routing_key='THMANI', body=json.dumps(mytrace))

    # on end stop
    if "END" in mytrace.keys():
        if mytrace["END"] == True:
            break 

connection.close()