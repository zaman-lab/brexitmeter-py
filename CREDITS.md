# Credits, Notes, and Reference

This is a (re)production of the [original @brexitmeter](https://twitter.com/brexitmeter).

## Neural Networks

### Keras and Tensorflow

The polarity classifier is a Keras model which uses a Tensorflow backend (CPU version).

  + [Keras Source](https://github.com/keras-team/keras)
  + [Tensorflow Source](https://github.com/tensorflow/tensorflow)
  + [Installing Tensorflow](https://www.tensorflow.org/install/pip)

## Natural Language Processing

### Gensim

"Gensim is a Python library for topic modeling, document indexing and similarity retrieval with large corpora."

  + [Gensim Source](https://github.com/RaRe-Technologies/gensim)
  + [Gensim Docs](https://radimrehurek.com/gensim/apiref.html)
  + [Gensim Quickstart](https://github.com/RaRe-Technologies/gensim/blob/develop/docs/notebooks/gensim%20Quick%20Start.ipynb)
  + [`Dictionary.load()`](https://radimrehurek.com/gensim/corpora/dictionary.html#gensim.corpora.dictionary.Dictionary.load)

### Wordsegment

"English word segmentation, written in pure-Python, and based on a trillion-word corpus."

  + [Wordsegment Source](https://github.com/grantjenks/python-wordsegment)

### Natural Language Toolkit (NLTK)

  + [NLTK Source](https://github.com/nltk/nltk)
  + [NLTK Notes](https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/packages/nltk.md)
  + [Installing NLTK dependencies on Heroku](https://devcenter.heroku.com/articles/python-nltk)

## Twitter

  + [Twitter API](https://developer.twitter.com/en/apps/)
  + [Twitter API Restricted Use Cases](https://developer.twitter.com/en/developer-terms/more-on-restricted-use-cases)
  + [Twitter API Response Codes](https://developer.twitter.com/en/docs/basics/response-codes)
  + [Twitter API Rate-limiting](https://developer.twitter.com/en/docs/basics/rate-limiting)

### Tweepy

  + [Tweepy](http://www.tweepy.org/)
  + [Tweepy Source](https://github.com/tweepy/tweepy)
  + [Tweepy Streaming Guide](http://docs.tweepy.org/en/v3.8.0/streaming_how_to.html)
  + [Tweepy `api.update_with_media()` Docs](http://docs.tweepy.org/en/v3.8.0/api.html?highlight=update_with_media#API.update_with_media)
  + [Tweepy `api.update_with_media()` Docs](http://docs.tweepy.org/en/v3.8.0/api.html?highlight=update_with_media#API.update_with_media) ... deprecated in favor of ...
  + [Tweepy `api.media_upload()` Docs](http://docs.tweepy.org/en/v3.8.0/api.html?highlight=update_with_media#API.media_upload)
  + [Tweepy `api.media_upload()` Example](https://stackoverflow.com/questions/51106363/tweet-mp4-files-with-tweepy)

## Heroku

We're hosting the production bot on a Heroku server.

  + [Heroku Python](https://devcenter.heroku.com/articles/getting-started-with-python)
  + [Google Application Credentials Buildpack](https://github.com/elishaterada/heroku-google-application-credentials-buildpack)

## Google Cloud Storage

The model weights file is [too big](https://stackoverflow.com/questions/44822146/githeroku-repository-or-object-not-found) to be pushed to Heroku, so on production we're going to be loading it from remote storage instead. We researched S3, and were close to getting it to work, but then found an existing [Google Cloud Storage integration with Keras](https://github.com/keras-team/keras/pull/11636/files), which made it really easy to load remote model files. :pray: tada:

  + [Making buckets public](https://cloud.google.com/storage/docs/access-control/making-data-public)
  + [Google Cloud Reference](https://cloud.google.com/python/docs/reference/)
  + [Google Cloud Storage Reference](https://cloud.google.com/storage/docs/reference/libraries)
