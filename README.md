# Brexitmeter Bot

A live twitter polarity bot. At-mention this account in a tweet, and we'll run the tweet text through our algorithm to classify the degree to which it expresses pro-Brexit sentiments.

## Files in this Repository

	README_brexitmeter.txt
	The present readme

	polarity_bot.py
	The main file to run the bot

	get_polarity.py
	A simple file that computes polarity of incoming tweet

	helper_text.py
	A simple file with methods to format incoming tweets
	to be sent through the neural network

	Final_weights
	The folder you get from training the neural net. Contains model weights.

	Dictionary
	The folder you get from training the neural net. Contains dictionaries.

	model.py
	The file containing model architecture. Loads dictionaries and weights.

	credentials.py
	A file containing your API credentials

	make_gauge.py
	A simple file to generate the gauge .png image the bot will attach
	to its answer

	Plots
	A folder in which plots will be stored

	up_gauge.png
	The  base gauge image file

## Introduction: what is the Brexitmeter code for?

The code implements a live Twitter bot with which users can interact to score tweet polarities on a given topic (examples: Brexit, US elections, YellowVests). For each event there should be one bot. In other words, Brexitmeter cannot score tweets about US election, as it is.

## What output to expect?

Once you run the code you might see updates printing in the shell as users query the bot. If you close the shell, the script dies and the bot stops answering to people. I ran it on MIT cluster. You could do the same on AWS.

## What input to feed the code?

First step is to train some neural network on a new dataset.

Train the neural network on a new event. Get the "model.py" file, along with "Final_weights" folder and "Dictionary" folder. Put that in this repository.

Then put your credentials in the "credentials.py" file.

You must now create a Twitter account for your bot, and make sure to change the `USER_HANDLE = "@brexitmeter"` line of "polarity_bot.py" to match the screen_name of the newly created bot account.

Now you can almost run the code...

## Pre-installing dependencies

Make sure to install the python libraries:

    tweepy
    PIL
    Keras

## Running the code

Finally simply run:

```sh
python3 polarity_bot.py
```
