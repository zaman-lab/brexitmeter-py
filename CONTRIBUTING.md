# Contributor's Guide

## Setup

Create and activate a virtual environment, using anaconda for example, if you like that kind of thing:

```sh
conda create -n brexit-env python=3.7 # (first time only)
conda activate brexit-env
```

Install all package dependencies using pip:

```sh
pip install -r requirements.txt # (first time only)
```

> see "requirements.txt" for a list of package dependencies

### Configuring Model File Storage

This app needs access to model artifact files, namely the final (pre-trained) weights, and two dictionaries of text.

You can download these files into this repo to access them locally, or configure google cloud storage to access them remotely.

 + set the `STORAGE_ENV` environment variable to "local" if you've downloaded the files into local storage, or "remote" to access the files hosted in google cloud storage
 + set the `GOOGLE_STORAGE_PATH` environment variable to our ["brexitmeter-bucket"](https://console.cloud.google.com/storage/browser/brexitmeter-bucket/), or to your own bucket that contains the model files
 + set `GOOGLE_APPLICATION_CREDENTIALS` to the path where your google service account credentials are. it should be an absolute path. even though you're using our model files, you'll still need to configure your api access credentials

> see "env.example" for a list of environment variables, with example values

### Configuring Twitter API Credentials

Create a Twitter account like "@brexitmeter_bot", and set it as the `TWITTER_BOT_HANDLE` environment variable.

Obtain credentials for your own app with access to the Twitter API, and set the following environment variables: `TWITTER_CONSUMER_KEY`, `TWITTER_CONSUMER_SECRET`, `TWITTER_ACCESS_TOKEN`, and `TWITTER_ACCESS_TOKEN_SECRET`

## Usage

After configuring model storage access to the model files, you can use the model to make predictions.

To test your ability to run the classifier, run the command-line client:

```sh
python -m app.client

# Tweet Text: I want to leave the EU
#> This tweet is [0.8231815] Pro Brexit

# Tweet Text: I want to stay in the EU
#> This tweet is [0.6230951] Pro Brexit
```

After configuring Twitter API credentials, you can run the Twitter Bot:

```sh
python -m app.bot
```

> then tweet at the bot's twitter handle and see the classification result in a reply tweet

## Testing

Install pytest:

```sh
pip install pytest # (first time only)
```

Run tests:

```sh
pytest --disable-pytest-warnings
```

## Deploying

> NOTE: the model weights file is too large to be deployed to heroku, so we need to load it from remote storage instead.

Create a new app server:

```sh
heroku create # (first time only)
```

Configure environment variables:

```sh
heroku config set STORAGE_ENV="remote"
# etc... (see all env vars in ".env.example" file)
```

Deploy:

```sh
git checkout gcs
git push heroku gcs:master
```

Run:

```sh
heroku run "python -m app.bot"
```
