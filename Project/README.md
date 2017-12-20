# Project Outline

## Create a Twitter Stream and send tweets to Spark
We set up the Spark context in local mode with 3 CPU's running simulating 3 different machines. And build a Spark streaming context based on Spark context and set the time interval to 5 seconds. So the incoming tweets will be collect into 1 RDD every 5 seconds.
```python
conf = SparkConf().setMaster('local[3]')
sc   = SparkContext(conf=conf)
ssc  = StreamingContext(sc, 5)
```

We build an app called TweetRead.py to pull tweet streaming from Twitter by using library called Tweepy and use socket to send streaming into Spark Streaming

```python
host = "localhost"      # Get local machine name
port = 5555             # Reserve a port for your service.
s = socket.socket()     # Create a socket object
s.bind((host, port))    # Bind to the port
s.listen(5)             # Now wait for client connection.
c, addr = s.accept()    # Establish connection with client.
```
We use Streaming Context API socketTextStream to receive tweet Streaming through port and transfer into Dstreaming, which is the Streaming of RDD
```python
raw_tweets = ssc.socketTextStream('localhost',5555)
```



## Clean Tweets

## Extract Feature Words

## Calculate Informativeness of Features

## Visualization

---

# Project Contributors:
#### [Caleb Hulburt](https://github.com/cmhulbert)
#### [Mohammad Azim](https://github.com/moazim1993)
#### [Xian Lai](https://github.com/Xianlai)
#### [Yao Jin](https://github.com/jinyaohh)


Group Project for Big Data Programming, Fall 2017

Project master repository: 
[Master Branch](<https://github.com/Xianlai/BigData_Spark>)
