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
  + [`Dictionary.load()`](https://radimrehurek.com/gensim/corpora/dictionary.html#gensim.corpora.dictionary.Dictionary.load)

### Wordsegment

"English word segmentation, written in pure-Python, and based on a trillion-word corpus."

  + [Wordsegment Source](https://github.com/grantjenks/python-wordsegment)

### Natural Language Toolkit (NLTK)

  + [NLTK Source](https://github.com/nltk/nltk)
  + [NLTK Notes](https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/packages/nltk.md)


On the server:


    Resource stopwords not found.
    Please use the NLTK Downloader to obtain the resource:

    >>> import nltk
    >>> nltk.download('stopwords')

    For more information see: https://www.nltk.org/data.html

    Attempted to load corpora/stopwords

    Searched in:
    - '/app/nltk_data'
    - '/app/.heroku/python/nltk_data'
    - '/app/.heroku/python/share/nltk_data'
    - '/app/.heroku/python/lib/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'
    **************************************************

OK [heroku was actually looking for the "nltk.txt" file](https://devcenter.heroku.com/articles/python-nltk), so adding it and trying again...

  + https://stackoverflow.com/questions/18385303/how-to-install-nltk-modules-in-heroku

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
  + https://cloud.google.com/python/docs/reference/
  + https://cloud.google.com/storage/docs/reference/libraries

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

## Deploying to Heroku

Normal `git push heroku gcs:master` fails due to something related to LFS:

> *Repository or object not found: https://git.heroku.com/brexitmeter-bot.git/info/lfs/objects/batch
> Check that it exists and that you have proper access to it
> Uploading LFS objects:   0% (0/1), 0 B | 0 B/s, done
> error: failed to push some refs to 'https://git.heroku.com/brexitmeter-bot.git'*

The model files are [too big](https://stackoverflow.com/questions/44822146/githeroku-repository-or-object-not-found) to be pushed to heroku, so we're going to load the model weights file from remote storage instead. We researched S3, and were close to getting it to work, but then found an existing [keras integration with google cloud storage](https://github.com/keras-team/keras/pull/11636/files). This amazing integration makes it really easy for keras to load remote model files. We're in business! :pray: tada:

Now to remove LFS from the repo:

  + remove / comment-out line in ".gitattributes"
  + `git lfs uninstall`
  + `mv model/final_weights.hdf5 ~/Desktop/`
  + update .gitignore, etc.
  + `mv ~/Desktop/final_weights.hdf5 model/`

Re-deploy:

```sh
git push heroku gcs:master
```

Alright. Here we go.

```sh
heroku run "python -m app.bot"
```
> FileNotFoundError: [Errno 2] No such file or directory: '/app/app/../dictionary/dic.txt'

Oh right, need to upload the dictionary files to GCS as well...

Checked them into the repo.

Oh, right, need to somehow upload credentials.json to Heroku...

```sh
heroku config:set GOOGLE_APPLICATION_CREDENTIALS="$(< credentials.json)"
```

Oh no this doesn't work. Getting error:
> 'File {} was not found.'.format(filename) google.auth.exceptions.DefaultCredentialsError

Need a way to [use keras' google storage integration with explicit credentials](https://stackoverflow.com/questions/58368853/keras-integration-with-google-cloud-storage-model-files-using-explicit-credenti), or need to run this app on Google App Engine instead of Heroku, and setup the app engine to have access to the api credentials.


EDIT:

[Oh wait maybe...](https://stackoverflow.com/questions/47446480/how-to-use-google-api-credentials-json-on-heroku)

  + [buildpacks](https://devcenter.heroku.com/articles/buildpacks#using-a-third-party-buildpack)


```sh
heroku config:set GOOGLE_CREDENTIALS="$(< credentials.json)"
heroku config:set GOOGLE_APPLICATION_CREDENTIALS="google-credentials.json"
heroku buildpacks:add https://github.com/elishaterada/heroku-google-application-credentials-buildpack
git push heroku gcs:master
```


OK, looks like its running, but then running out of memory after starting to load the weights.

> Process running mem=968M(189.1%)
> 2019-10-14T02:16:19.868897+00:00 heroku[bot.1]: Error R14 (Memory quota exceeded)
> 2019-10-14T02:16:30.384069+00:00 heroku[bot.1]: Process running mem=1279M(250.0%)
> 2019-10-14T02:16:30.408076+00:00 heroku[bot.1]: Error R15 (Memory quota vastly exceeded)
> 2019-10-14T02:16:30.413896+00:00 heroku[bot.1]: Stopping process with SIGKILL
> 2019-10-14T02:16:30.54627+00:00 heroku[bot.1]: Process exited with status 137
> 2019-10-14T02:16:30.587393+00:00 heroku[bot.1]: State changed from up to crashed
> 2019-10-14T02:17:50.329884+00:00 heroku[bot.1]: State changed from crashed to down


Maybe scale up the dynos...


  + https://devcenter.heroku.com/articles/dynos
  + https://devcenter.heroku.com/articles/procfile
  + https://devcenter.heroku.com/articles/dyno-types

```sh
heroku logs --ps bot

# heroku ps:resize bot=hobby #> free, hobby, standard-1x each have 512 MB.
# heroku ps:resize bot=standard-2x #>
heroku ps:resize bot=performance-m #>

# heroku ps:scale bot=2
```



Performance medium seems big enough to handle the job! Haha only $250/mo. Whaa.





Running into NLTK issues on the server, but getting closer.





## Deploying to Google App Engine

Create a new google app engine app from your project page in the google cloud console.

  + [Getting Started with App Engine Python 3.7](https://cloud.google.com/appengine/docs/standard/python3/runtime)
  + [Download the SDK (`gcloud` CLI)](https://cloud.google.com/sdk/docs/)
  + [Brew cask formula](https://formulae.brew.sh/cask/google-cloud-sdk)

```sh
brew cask install google-cloud-sdk
```

Login to your google cloud account, and pick the right project:

```sh
gcloud init
#> Your Google Cloud SDK is configured and ready to use!
```

Add an "app.yaml" file, then deploy to app engine:

```sh
gcloud app deploy
```

It adds the ".gcloudignore" file. Need to add an entry `"#!include:.gitignore"` to that file.

  + [Granting roles to service accounts](https://cloud.google.com/iam/docs/granting-roles-to-service-accounts)


```sh
gcloud app logs tail -s default
gcloud app logs read
```


/app/google-credentials.json
