import os
import time
import sys

from dotenv import load_dotenv

import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from app import APP_ENV
from app.model import load_model
from app.client import classify
from app.image_generator import save_brexit_image

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
        print(status.user.screen_name, "says:", status.text)

        if(BOT_HANDLE in status.text):
            # prevent bot loops - if we tweet the same person more than 10 times then start ignoring
            if(status.author.screen_name == self.lastTweeted):
                self.lastTweetedCount += 1
            else:
                self.lastTweeted = status.author.screen_name
                self.lastTweetedCount = 0

            if(status.in_reply_to_status_id is not None):
                return

            try:
                # rate limiting - if attempts is greater than 10, give up
                if(self.wait > 10):
                    print("TOO MUCH WAITING AROUND...", self.wait)
                    return
                elif(self.wait > 0):
                    print("SLEEPING FOR...", self.wait)
                    time.sleep(self.wait)

                message, media_filepath = self.compile_reply(status)
                print("MESSAGE:", message)

                request_params = {"status": message, "in_reply_to_status_id": status.id}
                if media_filepath and os.path.isfile(media_filepath):
                    upload_result = self.api.media_upload(media_filepath)
                    request_params["media_ids"] = [upload_result.media_id_string]
                    os.remove(media_filepath)

                response = self.api.update_status(**request_params) # ** converts a:b dict to a=b formatted params
                print("RESPONSE", type(response)) #> <class 'tweepy.models.Status'

                self.wait = 0
            except Exception as err:
                print("EXCEPTION", err)
                self.wait += 1
                return

    def compile_reply(self, status):
        message = f"@{status.author.screen_name} "
        media_filepath = None

        # remove the bot's handle... consider moving this logic into the classifier itself?
        print(status.text)
        tweet_text = status.text #> 'Testing the @brexitmeter_bot Oh yeah!'
        tweet_text = "".join(tweet_text.split(BOT_HANDLE)) #> 'Testing the  Oh yeah!'
        tweet_text = " ".join(tweet_text.split()) #> 'Testing the Oh yeah!'
        print(tweet_text)

        word_count = len(tweet_text.split(" "))
        if word_count <= 2:
            message += "Looks like this tweet is is only a few words..."
            message += " It's harder for me to infer polarity without more context " + u"\U0001F914"
            message += " Please try again!"
        else:
            result = classify(tweet_text, self.model) # pass in pre-loaded model to prevent re-loading
            print(result)
            score = result["pro_brexit"]
            if score > 0.4 and score < 0.6:
                message += " I think this tweet is either neutral or I have never seen such language before " + u"\U0001F644"
            else:
                message += f" I think this tweet is {str(int(score*100))}% Pro-Brexit"
                media_filepath = save_brexit_image(score)

        if APP_ENV != "production":
            message += f" [env:{APP_ENV}]"

        return message, media_filepath

    def on_error(self, status_code):
        print("ON ERROR:", status_code)

    def on_timeout(self):
        print("TIMEOUT!")
        return True # don't kill the stream!

if __name__ == '__main__':

    print("APP ENV", APP_ENV)

    listener = StdOutListener()
    print("LISTENER", type(listener))

    stream = Stream(listener.auth, listener)
    print("STREAM", type(stream))

    stream.filter(track=[BOT_HANDLE])

    # this never gets reached
