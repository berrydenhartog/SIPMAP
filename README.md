# SIPMAP
This is a prototype to show how SIPMAP could be transformed from one huge application to operation services. Making it's operations Async, cloud ready and program language agnostic.

If this change is done new operations can be fully decoupled from frame, meaning any researcher, programmer or user could write a quick plug-in. They will only need to be able to accept messages from a queue in a standardized format. 

Another benefit is that you can optimize workflows. When working with queues you can see where the queues start to build up. If this happens you could choose to start more operation of the same type, sharing the load. This could decrease the overall time.  

# Running the examples
Before running the prototype please install docker.io and docker-compose. 
 ```
  apt install docker.io docker-compose
```

To run the example do the following:
 ```
    cd <NormalFlow|ParallelFlow|FanoutFlow>
    docker-compose build
    docker-compose up
 ```

# Examples
## NormalFlow
This prototype is using DSCIN, THMANI and DSCOUT. It runs rabbitmq and all operation in ASYNC. i choose to build the prototype in python because this develops faster. The real deal should be written in c or c++ and needs fortran wrappers so we can integrate it into frame. 

## ParallelFlow
Same as NormalFlow but THMANI runs parallel reading the queues with 2 workers sharing the load.

## FanoutFlow
TODO. Same as NormalFlow but THMANI runs parallel both reading the same data. 

# Which protocol: JSON or Protobuf
This example is written with JSON. Protobuf would be a better solution when implementing this because of the performance gains. Especially when handling allot of data. 

# Which message queue
[RabbitMQ](https://www.rabbitmq.com/devtools.html) or [Kafka](https://kafka.apache.org/). If you want to have history use Kafka. 

# The idea for SSF traces and SQSAF data
The general idea is to use a message broker as handler for the traces/SQSAF. So a operation pushes a trace/SQSAF to frame, frame takes it from IAR and puts it in a JSON/PROTOBUF format and puts it into Rabbitmq. another operation reads the traces from the queue and puts it in IAR. FRAME will still do all other things it always did like DISC7, Memory management etc. 

# The idea for SIGNAR and SAF then
Rabbitmq has 'exchanges' and queues on these exchanges. we could make a trace exchange, a saf exchange, sqsaf exchange and signar exchange. Since queues allow us to filter message, we can only extract the message with the correct SAFID or SIGNAR id. Frame would build up the SAF file as it always did in the preparation phase, and sends to rabbitmq when done. Another operation reads this queue and waits until the correct SAF file passes by. It then reads the SAF file and goes to the execution phase. 

# The idea for HistoryHeader
same as SAF

# getting from a deck to a workflow
We will need to create a script that converts a DECK to a docker-compose.yml file. It should split all the operation cards and store it either as a file or environmental variable. The card number needs to be saved as an environmental variable because we will use this to setup the queues.

# special operations
## PARSTR
using a fanout exchange will be similar to how PARSTR works now

## SIPIO
Not needed anymore because this is done by rabbitmq

## SAVEIT
saveit is used to pass information from one operation to another, i would not recommend porting this operation, but if you do, you could use a key value store 

# Notes
## possible issues
One major issue will be operations communicating through common blocks. If this happens they must be uncoupled or bundled.

Another issue could be the expiration of messages. 

## Docker's
We can choose to make every operation a separate executable, but it would be better manageable if we use dockers. In docker you can attach version's to the docker file and save them in a docker registry like [harbor](https://goharbor.io/). Examples:
```
   sipmap/thmani:202001
   sipmap/thmani:202003
   sipmap/thmani:202003-1
   sipmap/thmani:1.0.0
   sipmap/thmani:latest
   sipmap/thmani:dev
   sipmap/thmani:prod
```
When we save the docker images in a registry like this every user can choose per operation which version he would like to use. the default could be prod. I would recommend moving away from the old method of versioning where we use the year and month and move to an official versioning scheme for major,minor and patches. and then use prod and dev to switch between production and development dockers. 

## Message Passing Interface
MPI will only be needed for specific operations. I would recommend adding IFDEFS around the code in frame and only build it for the operations that needed it. 


## RABBITMQ management console
management console is available here: http://localhost:15672/
login: guest,guest

