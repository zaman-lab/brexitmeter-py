# Contributor's Guide


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
python app/classifier.py
# Tweet Text: I want to leave the EU
#> This tweet is [0.8231815] Pro Brexit

# Tweet Text: I want to stay in the EU
#> This tweet is [0.6230951] Pro Brexit
```

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
