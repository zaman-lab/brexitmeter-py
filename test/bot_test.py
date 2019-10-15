
from tweepy.auth import OAuthHandler
from tweepy.streaming import Stream

from app.bot import StdOutListener, Stream

def test_listener():
    listener = StdOutListener()
    assert isinstance(listener.auth, OAuthHandler)

def test_stream():
    listener = StdOutListener()
    stream = Stream(listener.auth, listener)
    assert isinstance(stream, Stream)
