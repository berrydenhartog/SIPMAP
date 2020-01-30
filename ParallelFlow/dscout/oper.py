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
channel.queue_declare(queue='THMANI')

# get traces
for method_frame, properties, body in channel.consume('THMANI'):

    #Receive trace from DSCIN
    mytrace = json.loads(body)
    print("DSCOUT" + json.dumps(mytrace), flush=True)
    print(mytrace)

    # call fortran operation 

    # on end stop
    if "END" in mytrace.keys():
        if mytrace["END"] == True:
            break 

connection.close()