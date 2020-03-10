#!/usr/bin/python3
from confluent_kafka import Consumer, KafkaError
import json

print("starting consumer", flush=True)
consumer = Consumer({
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})


################ preperation phase
consumer.subscribe(['thmanihh'])
while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    myhistoryheader = json.loads(msg.value().decode('utf-8'))
    print("dscout history header" + json.dumps(myhistoryheader), flush=True)
    break

################ execution phase
consumer.subscribe(['thmanitraces'])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    mytrace = json.loads(msg.value().decode('utf-8'))
    print("THMANI" + json.dumps(mytrace), flush=True)

    # call fortran operation 


    # on end stop
    if "END" in mytrace.keys():
        if mytrace["END"] == True:
            break 

consumer.close()