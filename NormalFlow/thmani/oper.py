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

# setup exchanges
channel.exchange_declare(exchange='traces', exchange_type='direct')
channel.exchange_declare(exchange='historyheader', exchange_type='topic')

# check if queue exist. else create
inqueue = channel.queue_declare(queue='DSCIN',auto_delete=True)
outqueue = channel.queue_declare(queue='THMANI',auto_delete=True)
inhhqueue = channel.queue_declare(queue='HHDSCIN',auto_delete=True)
outhhqueue = channel.queue_declare(queue='HHTHMANI',auto_delete=True)

# bind a queue to an exchange
channel.queue_bind(exchange='traces',
                   queue=inqueue.method.queue)
channel.queue_bind(exchange='traces',
                   queue=outqueue.method.queue)
channel.queue_bind(exchange='historyheader',
                   queue=inhhqueue.method.queue,
                   routing_key="DSCIN.historyheader")
channel.queue_bind(exchange='historyheader',
                   queue=outhhqueue.method.queue,
                   routing_key="THMANI.historyheader")
    

################ preperation phase
for method_frame, properties, body in channel.consume(inhhqueue.method.queue):
    myhistoryheader = json.loads(body)
    print("THMANI history header" + json.dumps(myhistoryheader), flush=True)

    channel.basic_publish(exchange='historyheader', routing_key='THMANI.historyheader', body=json.dumps(myhistoryheader))
    
    break

channel.close()
channel = connection.channel()

################ execution phase
for method_frame, properties, body in channel.consume(inqueue.method.queue):

    mytrace = json.loads(body)
    print("THMANI" + json.dumps(mytrace), flush=True)

    # call fortran operation    

    # Send trace to next operation
    channel.basic_publish(exchange='traces', routing_key='THMANI', body=json.dumps(mytrace))

    # on end stop
    if "END" in mytrace.keys():
        if mytrace["END"] == True:
            break 

connection.close()