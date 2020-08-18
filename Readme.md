# Arrow flight tests
Simple test looking at arrow + arrow flight
Consists of server.py and client.py ( copied in part from arrow docs )

## Requirements 
Python 3.8.x

## Running

```
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
python server.py
```

In a seperate terminal

Load a CSV
```
source ./venv/bin/activate
python client.py put 0.0.0.0:5005 monroe-county-crash-data2003-to-2015.csv.gz  
```

List flights
```
python client.py list 0.0.0.0:5005
```


Get flight ( dataset )
```
 python client.py get 0.0.0.0:5005 -p monroe-county-crash-data2003-to-2015.csv.gz
```

Query 
```
?????
```

## NOTES..
https://mirai-solutions.ch/news/2020/06/11/apache-arrow-flight-tutorial/
https://github.com/ballista-compute/ballista
https://www.tutorialandexample.com/apache-arrow-tutorial/

https://www.youtube.com/watch?v=5o5E-CfC8gw

Thinking arrow table is the interface, see it in java, golang, nodejs etc..


batch versus table ?
```
type Table interface {
    Schema() *arrow.Schema
    NumRows() int64
    NumCols() int64
    Column(i int) *Column

    Retain()
    Release()
}
```
The containers in a Pod can also communicate with each other using standard inter-process communications like SystemV semaphores or POSIX shared memory. Containers in different Pods have distinct IP addresses and can not communicate by IPC without special configuration. Containers that want to interact with a container running in a different Pod can use IP networking to communicate.

Can I have a sidecar share memory..  data client & program sharing memory ?
https://kubernetes.io/docs/concepts/workloads/pods/
```
The containers in a Pod can also communicate with each other using standard inter-process communications like SystemV semaphores or POSIX shared memory. Containers in different Pods have distinct IP addresses and can not communicate by IPC without special configuration. Containers that want to interact with a container running in a different Pod can use IP networking to comunicate.
```
##
Authentication
Flight tickets
Multiple endpoints ?


## Spark
https://github.com/rymurr/flight-spark-source

PUSH Downs ?? 


## Postgres
https://github.com/heterodb/pg2arrow
http://heterodb.github.io/pg-strom
