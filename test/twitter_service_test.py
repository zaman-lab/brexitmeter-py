import tweepy

from app.bot import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET, BOT_HANDLE

def test_api_client():

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    assert "update_status" in dir(api)
    assert "media_upload" in dir(api)

    #user = api.verify_credentials()
    #assert isinstance(user, tweepy.models.User)
