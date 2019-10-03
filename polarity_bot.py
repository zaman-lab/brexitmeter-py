#!/usr/bin/env python
#coding: utf8 
 
import tweepy, time, sys, re, json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import matplotlib
matplotlib.use('Agg')
from model import load_model
from get_polarity import compute_polarity
model = load_model()
import matplotlib.pyplot as plt
from matplotlib import cm, gridspec
import numpy as np
import math
from PIL import Image
from mpl_toolkits.axes_grid1 import make_axes_locatable
from make_gauge import plotGauge2
import os

#API KEYS - Fill these in from Twitter. 

with open('credentials.py') as f:
    lines = f.read().splitlines()

CONSUMER_KEY = lines[0]
CONSUMER_SECRET = lines[1]
ACCESS_KEY = lines[2]
ACCESS_SECRET = lines[3]
USER_HANDLE = "@brexitmeter"


class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def __init__(self):
        self.wait = 0
        self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        self.api = tweepy.API(self.auth)
        self.lastTweeted = ""
        self.lastTweetedCount = 0

    def on_status(self, status):
        # try:
        print (status.text)
        print (status.user.screen_name)

        if(USER_HANDLE  in status.text):

            tweetText_ = status.text.split(USER_HANDLE)


            tweetText = ''.join([i for i in tweetText_ if USER_HANDLE not in i])

            temp=tweetText.split(' ')[1:]

            #sort out any white spaces left over from splitting
            #account for if username is at the start of a tweet/in the middle/at the end

            tweetText = ''.join(tweetText)

            score=compute_polarity(tweetText,model)[0]
            plotname=plotGauge2(score, status.author.screen_name)

            withPics=False
            print(temp)
            if(len(temp)<=2):
                postMsg = '@' + status.author.screen_name + " Looks like this tweet is is only a few words... it's harder for me to infer polarity without more context "+ u"\U0001F914" 
            else:
                if(score < 0.6 and score > 0.4):
                    postMsg = '@' + status.author.screen_name + " I think this tweet is either neutral or I have never seen such language before " + u"\U0001F644" 
                else:    
                    postMsg = '@' + status.author.screen_name + " I think this tweet is " + str(int(score*100)) +  " % Pro Brexit"
                    withPics=True



            #prevent bot loops - if we tweet the same person more than 10 times then start ignoring. 
            if(status.author.screen_name == self.lastTweeted):
                self.lastTweetedCount += 1
            else:
                self.lastTweeted = status.author.screen_name
                self.lastTweetedCount = 0

            if(status.in_reply_to_status_id is not None):
                return



            #rate limiting - if attempts is greater than 10, give up
            try:
                if(self.wait > 10):
                    return
                elif(self.wait > 0):
                    time.sleep(self.wait)
                self.api.update_with_media(filename='plots/'+plotname,status=postMsg, in_reply_to_status_id=status.id)

                self.wait = 0
            except Exception as a:
                print(a)
                self.wait += 1
                return

            except Exception as  e:
                print(e)
                return

            if os.path.exists('plots/'+plotname):
                os.remove('plots/'+plotname)


    def on_error(self, status):
        print(status)
        print (sys.stderr + ' Encountered error with status code: ' + status_code)
    
    def on_timeout(self):
        print (sys.stderr + 'Timeout...')
        return True # Don't kill the stream



if __name__ == '__main__':
    l = StdOutListener()

    print('initiated')

    stream = Stream(l.auth, l)

    stream.filter(track=['@brexitmeter'])



