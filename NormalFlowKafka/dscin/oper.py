#!/usr/bin/python3
from confluent_kafka import Producer
import json

print("starting producer", flush=True)
producer = Producer({'bootstrap.servers': 'kafka:9092'})


############### preperation phase
print("sending historyheader", flush=True)
history_header={
    "VERSION": 1.0
}
producer.produce("dscinhh", value=json.dumps(history_header), key="dscin")

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
    producer.produce("dscintraces", value=json.dumps(trace),key="dscin")
    producer.flush()

# send end of data 
producer.produce("dscintraces", value=json.dumps({"END":True}),key="dscin")
producer.flush()