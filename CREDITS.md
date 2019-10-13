# Credits, Notes, and Reference

This is a (re)production of the original @brexitmeter created by ____________.

## Neural Network

### Keras and Tensorflow

The polarity classifier is a Keras model which uses a Tensorflow backend (CPU version).

  + [Keras Source](https://github.com/keras-team/keras)
  + [Tensorflow Source](https://github.com/tensorflow/tensorflow)
  + [Installing Tensorflow](https://www.tensorflow.org/install/pip)

## Natural Language Processing

### [Gensim](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=9vG_kV0AAAAJ&citation_for_view=9vG_kV0AAAAJ:NaGl4SEjCO4C)

"Gensim is a Python library for topic modeling, document indexing and similarity retrieval with large corpora."

  + [Gensim Source](https://github.com/RaRe-Technologies/gensim)
  + [Gensim Docs](https://radimrehurek.com/gensim/apiref.html)
  + [Gensim Quickstart](https://github.com/RaRe-Technologies/gensim/blob/develop/docs/notebooks/gensim%20Quick%20Start.ipynb)

### Wordsegment

"English word segmentation, written in pure-Python, and based on a trillion-word corpus."

  + [Wordsegment Source](https://github.com/grantjenks/python-wordsegment)

### Natural Language Toolkit (NLTK)

  + [NLTK Source](https://github.com/nltk/nltk)
  + [NLTK Notes](https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/packages/nltk.md)

## Twitter

  + [Twitter API](https://developer.twitter.com/en/apps/)
  + [Twitter API Restricted Use Cases](https://developer.twitter.com/en/developer-terms/more-on-restricted-use-cases)

## Amazon S3

  + [S3 Boto Python Package Source](https://github.com/boto/boto3)
  + [Tutorial](https://realpython.com/python-boto3-aws-s3/)
  + [S3 API Docs](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html)
  + [`S3.Client.get_object`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.get_object)
  + [`S3.ServiceResource.Buckets`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.buckets)
  + [`S3.Object`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#object)

## Google Cloud Storage

  + [Making buckets public](https://cloud.google.com/storage/docs/access-control/making-data-public)

<hr>

## Git Large File Storage

The model file is too large for normal Git, so in order to push to GitHub, we need to use [Git Large File Storage](https://git-lfs.github.com/).

Install on a Mac via Homebrew, if necessary:

```sh
brew install git-lfs # (first time only)
```

From within the repo's root directory, when it doesn't yet contain the model file, install and configure Git Large File Storage:

```sh
git lfs install
git lfs track "*.hdf5"
git add .gitattributes
```

> NOTE: if your repo already has the model file checked in, I found I needed to actually `rm -rf .git` and create a new commit history in order for this to work. WARNING: this is a destructive action, as it will remove the previous commit history.

Then add the model file and commit as normal, and you should be able to push:

```sh
mv ~/Desktop/final_weights.hdf5 Final_weights/
git add .
git commit -m "Configure Git Large File Storage, and add the model file"
git push origin master
```

## Deploying Large Files to Heroku

Normal `git push heroku master` fails due to "". See [this post](https://stackoverflow.com/questions/44822146/githeroku-repository-or-object-not-found)
