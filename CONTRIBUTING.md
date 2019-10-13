# Contributor's Guide

## Prerequisites

### Amazon S3

Gain access to the model file. Observe it's object URL, and set the environment variable `MODEL_FILE_URL` accordingly.

## Setup

```sh
conda create -n brexit-env python=3.7 # (first time only)
conda activate brexit-env
```

```sh
pip install -r requirements.txt # (first time only)
```

## Usage

Classify your own user-provided text:

```sh
python -m app.client
# Tweet Text: I want to leave the EU
#> This tweet is [0.8231815] Pro Brexit

# Tweet Text: I want to stay in the EU
#> This tweet is [0.6230951] Pro Brexit
```

See the contents of the model's dictionaries:

```sh
python -m app.dictionaries
```

Run the Twitter Bot:

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
heroku config set MODEL_ENV="remote"
# etc.
```
```


Deploy:

```sh
git checkout reorg-bot-deploy
git push heroku master
```
