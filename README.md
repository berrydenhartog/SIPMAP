# SIPMAP

# Running the prototype
To run the prototype please install docker.io and docker-compose.yml. 
Make sure you have an internet connection. 

You can start an example by going in a Example and type:
 - docker-compose build
 - docker-compose up

# current examples:
NormalFlow: Example using DSCIN, THMANI and DSCOUT. It runs rabbitmq and all operation in ASYNC. i choose to build the prototype in python because this develops faster. The real deal should be written in c or c++ and needs fortran wrappers so we can integrate it into frame. 

ParallelFlow: Same as NormalFlow but THMANI runs parallen reading the queus with 2 workers sharing the load. In theory you can add any number of workers.

# The idea for SSF and SQSAF
The general idea is to use rabbitmq as handler for the traces/SQSAF. So a operation pushes a trace/SQSAF to frame, frame then takes it from IAR and puts it in a JSON format and puts it into Rabbitmq. another operation reads the traces from the queue and puts it in IAR. FRAME will still do all other things it always did. 

Since rabbitmq is async and will run next to SIPMAP, and every operation gets its own queue where the name is based on the jobid and the cardnumber (based from the original deck). It could all work async. The only thing left to do is make every operation its own executable. the operations will wait for traces to arive in the queue and processes them when they are available. 

If we want something to be processed faster we could add two operations to the same queue. this will work directly for single trace operations. for panel operation we will propably need to add a special panel operation before the queue so every operation gets a whole panel.

# but what about SIGNAR and SAF then
We could do two things with SAF/SIGNAR. We could add a REDIS service where we can store and get SAF files. the key would be JOBID_SAFNAM. But the other, and in my oppinion the best, would be to use RabbitMQ. Rabbitmq has 'exchanges' and queues on these exchanges. we could make a trace exchange, a saf exchange, sqsaf exchange and signar exchange. Since queues allow us to filter message, we can only extract the message with the correct SAF file. Frame would build up the SAF file as it always did in the preperation phase, and sends to rabbitmq when done. Another operation reads this queue and waits untill the correct SAF file passes by. It then reads the SAF file and goes to the execution phase. 

# RABBITMQ
management console is available here: http://localhost:15672/
login: guest,guest

# special operations
## PARSTR
using a fanout exchange will be similair to how PARSTR works now

