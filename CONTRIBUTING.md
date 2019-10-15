# Contributor's Guide

Hey, so you want to run this app yourself? Great. Follow the instructions in this guide.

## Installation

Create and activate a virtual environment, using anaconda for example, if you like that kind of thing:

```sh
conda create -n brexit-env python=3.7 # (first time only)
conda activate brexit-env
```

Install package dependencies:

```sh
pip install -r requirements.txt # (first time only)
```

## Setup

Create a ".env" file and set your environment variables there. See the ".env.example" file for examples, and sections below for more details.

### Model File Storage

To classify text, this app needs access to a file of the model's final weights, which we're hosting in a publicly-available Google Cloud Storage bucket called["brexitmeter-bucket"](https://console.cloud.google.com/storage/browser/brexitmeter-bucket/)".

Feel free to use the files in this bucket (i.e. "remote" storage option), or download them into your local repository for faster file-load times (i.e. "local" storage option). Depending on which storage option you choose ("local" or "remote"), set the environment variable `STORAGE_ENV` accordingly.

If choosing the "remote" storage option: download your Google Cloud API service account credentials and set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable accordingly.

After configuring your storage option, run the storage service to verify all files are in place:

```sh
python -m app.storage_service

#> True
#> True
# etc...
```

Run the dictionaries parser to inspect the word lists the model is using:

```sh
python -m app.dictionaries

#> ()
#> ()
# etc...
```

OK, model setup complete! If you'd like to start using the classifier via a lightweight command-line interface, you can skip to the "usage" section below.

### Twitter Bot Setup

Create a Twitter account with a handle like ["@brexitmeter_bot"](https://twitter.com/brexitmeter_bot), and set the `TWITTER_BOT_HANDLE` environment variable accordingly.

Obtain credentials for your own app with access to the Twitter API, and set the environment variables `TWITTER_CONSUMER_KEY`, `TWITTER_CONSUMER_SECRET`, `TWITTER_ACCESS_TOKEN`, and `TWITTER_ACCESS_TOKEN_SECRET` accordingly.

## Usage

Run the classifier via an interactive command-line client:

```sh
APP_ENV="development" python -m app.client

# Tweet Text: I want to leave the EU
#> This tweet is [0.8231815] Pro Brexit

# Tweet Text: I want to stay in the EU
#> This tweet is [0.6230951] Pro Brexit
```

Run the classifier via an interactive Twitter Bot, which will reply to at-mentions with the classification of the tweet's text:

```sh
python -m app.bot
```

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

Create a new app server:

```sh
heroku create # (first time only)
```

Configure environment variables:

```sh
heroku config set APP_ENV="production"
heroku config set STORAGE_ENV="remote"
# etc...
```

Deploy:

```sh
git checkout master
git push heroku master
```

Test everything is working in production:

```sh
heroku run "python -m app.storage_service"
heroku run "python -m app.dictionaries"
heroku run "python -m app.client"
```

Run the bot in production:

```sh
heroku run "python -m app.bot"
```
