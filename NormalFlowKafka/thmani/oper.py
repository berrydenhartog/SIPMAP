#!/usr/bin/python3
from confluent_kafka import Producer, Consumer, KafkaError
import json

print("starting producer", flush=True)
producer = Producer({
    'bootstrap.servers': 'kafka:9092'
})
print("starting consumer", flush=True)
consumer = Consumer({
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})


################ preperation phase
consumer.subscribe(['dscinhh'])
while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    myhistoryheader = json.loads(msg.value().decode('utf-8'))
    print("THMANI history header" + json.dumps(myhistoryheader), flush=True)
    producer.produce("thmanihh", value=json.dumps(myhistoryheader), key="thmani")
    break

################ execution phase
consumer.subscribe(['dscintraces'])

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

    # Send trace to next operation
    producer.produce("thmanitraces", value=json.dumps(mytrace), key="thmani")
    producer.flush()


    # on end stop
    if "END" in mytrace.keys():
        if mytrace["END"] == True:
            break 

consumer.close()