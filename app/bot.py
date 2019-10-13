import os
import time
import sys

from dotenv import load_dotenv

import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from app.model import load_model
from app.client import compute_polarity
#from make_gauge import plotGauge2

load_dotenv()

CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY", default="OOPS")
CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET", default="OOPS")
ACCESS_KEY = os.getenv("TWITTER_ACCESS_TOKEN", default="OOPS")
ACCESS_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET", default="OOPS")
BOT_HANDLE = os.getenv("TWITTER_BOT_HANDLE", default="@brexitmeter_bot")

class StdOutListener(StreamListener):
    """ Opens a connection with the Twitter API, handles a stream of specified tweet events."""

    def __init__(self):
        """model: keras model with weights loaded, ready to make predictions"""
        self.wait = 0
        self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        self.api = tweepy.API(self.auth)
        self.lastTweeted = ""
        self.lastTweetedCount = 0
        self.model = load_model()

    def on_status(self, status):

        print("----------------")
        print("DETECTED AN INCOMING TWEET!")
        print(status.text)
        print(status.user.screen_name)

        if(BOT_HANDLE in status.text):

            tweetText_ = status.text.split(BOT_HANDLE)
            tweetText = ''.join([i for i in tweetText_ if BOT_HANDLE not in i])
            temp=tweetText.split(' ')[1:]
            print(temp)
            #sort out any white spaces left over from splitting
            #account for if username is at the start of a tweet/in the middle/at the end
            tweetText = ''.join(tweetText)

            if(len(temp)<=2):
                message = '@' + status.author.screen_name + " Looks like this tweet is is only a few words... it's harder for me to infer polarity without more context "+ u"\U0001F914"
            else:
                result = compute_polarity(tweetText, self.model) # pass in the pre-loaded model to prevent re-loading
                print(result) #> ndarray with shape (1, 2)
                score = result[0][1]
                #plotname=plotGauge2(score, status.author.screen_name)
                print(score)

                if score > 0.4 and score < 0.6:
                    message = '@' + status.author.screen_name + " I think this tweet is either neutral or I have never seen such language before " + u"\U0001F644"
                else:
                    message = '@' + status.author.screen_name + " I think this tweet is " + str(int(score*100)) +  " % Pro Brexit"

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

                #media_filepath = os.path.join(path.dirname(__file__), "..", "img", "up_gauge.png")
                media_filepath = os.path.join(os.path.dirname(__file__), "..", "img", "up_gauge.png")
                self.api.update_with_media(
                    filename = media_filepath,
                    status = message,
                    in_reply_to_status_id = status.id
                )

                self.wait = 0
            except Exception as a:
                print(a)
                self.wait += 1
                return

            except Exception as  e:
                print(e)
                return

            #if os.path.exists(media_filepath):
            #    os.remove(media_filepath)

    def on_error(self, status):
        print(status)
        print (sys.stderr + ' Encountered error with status code: ' + status_code)

    def on_timeout(self):
        print (sys.stderr + 'Timeout...')
        return True # Don't kill the stream

if __name__ == '__main__':

    listener = StdOutListener()
    print("LISTENER...", type(listener))

    stream = Stream(listener.auth, listener)
    print("STREAM", type(stream))

    stream.filter(track=[BOT_HANDLE])

    breakpoint() # this never gets reached. the stream is connected
