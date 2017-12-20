#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implementation of tweets listener based on tweepy API.

Date: Nov.15, 2017
"""

from tweepy import OAuthHandler, API, Stream
from tweepy.streaming import StreamListener
import socket

tracks = ['maga', 'resist'] # The topics of tweets to receive
host   = "172.17.0.2"       # the IP address of local host


consumer_key    = "GfUirs5Qb88kcqI67AyIbcCix"
consumer_secret = "8YJ64NwbywQVAxcYpcHGrmlk9Ahkb5Plv1TOSmdWnjm5poLN4H"
access_token    = "595598668-i0vBACxNaQtzMlUM7sOhLw2vboynfgwzLjAElJX8"
access_secret   = "gzV7S4PjD3YBTktgjdBgs9oe5c7a5iaPHN4sl12d1jRAD"

class Listener(StreamListener):

    def __init__(self, csocket, api):
        self.client_socket = csocket
        self.api = api
 
    def on_status(self, status):
        """ handles the incoming tweets by first filtering and then forward to
        socket.

        inputs:
        -------
        - status: the in-coming tweet object itself with many attributes all 
            stored in JSON format. For more attributes of tweet object, -> 
            <https://developer.twitter.com/en/docs/tweets/data-dictionary/
            overview/tweet-object>
        """
        # discards the tweets that are either truncated or not in english
        # if status.truncated or status.lang != "en": return

        # reads the text attribute of status object
        # forward to the client socket provided
        try:
            if status.text != '':
                tmsg = status.text.encode('utf-8')    # encode
                self.client_socket.send(tmsg)
            return True
        # if an exception occurred between connection with spark like broken
        # pipe, stop pulling tweets
        except BaseException as e:
            print("Error on_status: %s" % str(e))
            return False

        return True
 
    def on_error(self, status):
        """ if there is an error occured between connection with tweepy, stop
        pulling tweets.
        """
        print(status)
        return False


def sendData(c_socket=None):
    # set up api and authorization for receiving tweets
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = API(auth)
 
    print("sending tweets...")
    
    # receive tweets on assigned tracks, 
    # filter them by assigned conditions and send them to port
    twitter_stream = Stream(auth, Listener(c_socket, api))
    twitter_stream.filter(track=tracks)


if __name__ == "__main__":

    s = socket.socket()     # initial a socket object
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, 5555))    # bind to the port connected with Spark
 
    print("Listening on port: 5555")
 
    s.listen(5)             # Now wait for client connection.
    c, addr = s.accept()    # Establish connection with client.
 
    print("Received request from: " + str(addr))
 
    sendData(c_socket=c)


