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

            tweetText_ = status.text.split(BOT_HANDLE)
            tweetText = ''.join([i for i in tweetText_ if BOT_HANDLE not in i])
            temp = tweetText.split(' ')[1:]
            #sort out any white spaces left over from splitting
            #account for if username is at the start of a tweet/in the middle/at the end
            tweetText = ''.join(tweetText)
            #print("temp", temp) #> ['', 'in', 'development,', 'this', 'might', 'not', 'work', '2']
            #print("tweetText", tweetText) #> testing  in development, this might not work 2
            print(tweetText.split(' '))

            message, media_filepath = self.compile_reply(status, temp, tweetText)
            print("MESSAGE:" message)

            # prevent bot loops - if we tweet the same person more than 10 times then start ignoring
            if(status.author.screen_name == self.lastTweeted):
                self.lastTweetedCount += 1
            else:
                self.lastTweeted = status.author.screen_name
                self.lastTweetedCount = 0

            if(status.in_reply_to_status_id is not None):
                return

            #
            # SEND THE TWEET!
            #

            try:
                #rate limiting - if attempts is greater than 10, give up
                if(self.wait > 10):
                    return
                elif(self.wait > 0):
                    time.sleep(self.wait)

                #self.api.update_with_media(
                #    filename=media_filepath,
                #    status=message,
                #    in_reply_to_status_id=status.id
                #)
                # FYI: update_with_media is deprecated, use media_upload() instead

                request_params = {"status": message, "in_reply_to_status_id": status.id}
                if media_filepath:
                    upload_result = self.api.media_upload(media_filepath)
                    request_params["media_ids"] = [upload_result.media_id_string]

                response = self.api.update_status(**request_params) # ** converts a:b dict to a=b formatted params
                print("RESPONSE", type(response)) #> <class 'tweepy.models.Status'

                self.wait = 0
            except Exception as a:
                print(a)
                self.wait += 1
                return
            except Exception as e:
                print(e)
                return

            #
            # CLEAN UP
            #

            if media_filepath and os.path.exists(media_filepath):
                os.remove(media_filepath)

    def compile_reply(self, status, temp, tweet_text):
        message = f"@{status.author.screen_name} "
        media_filepath = None

        if (len(temp) <= 2):
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

        if APP_ENV is not "production":
            message += f" [env:{APP_ENV}]"

        return message, media_filepath

    def on_error(self, status_code):
        print("ERROR! ...", status_code)
        print(sys.stderr)

    def on_timeout(self):
        print("TIMEOUT!")
        print(sys.stderr)
        return True # don't kill the stream!

if __name__ == '__main__':

    #auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    #auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    #api = tweepy.API(auth)

    listener = StdOutListener()
    print("LISTENER...", type(listener))

    stream = Stream(listener.auth, listener)
    print("STREAM", type(stream))

    stream.filter(track=[BOT_HANDLE])

    # this never gets reached
