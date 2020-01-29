# SIPMAP

# Running the prototype
To run the prototype please install docker.io and docker-compose.yml. 
Make sure you have an internet connection. 

You can start the example by running 
 - docker-compose build    (in the root of this folder)
 - docker-compose up

# The idea
The general idea is to use rabbitmq as handler for the traces. So frame just passes the traces from IAR to rabbitmq and the reverse. 

Since rabbitmq is async and will run next to SIPMAP, and every operation gets its own queue where the name is based on the jobid and the cardnumber (based from the original deck). It could all work async. The only thing left to do is make every operation its own executable. the operations will wait for traces to arive in there queue and processes them when they are available. 

This will almost be like a RESTFULL service, however it will still have state because we parse it traces, and not all the input the operation requires. This could be solved by passing more then one trace at a time. 

# but what about SAF then?
We could do two things with SAF. one would be to make DISK7 files available to all processes (by volumizing the disk folder) or better, we could add a REDIS service. Where we can store and get SAF files. the key would be JOBID_SAFNAM. 

# RABBITMQ
management console is available here: http://localhost:15672/
login: guest,guest


