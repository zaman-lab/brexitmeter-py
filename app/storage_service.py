

import os
from dotenv import load_dotenv
from google.cloud import storage

load_dotenv()

STORAGE_ENV = os.getenv("STORAGE_ENV", default="local") # "local" OR "remote"
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", default="OOPS") # implicit check by google.cloud (and keras)
GOOGLE_STORAGE_PATH=os.getenv("GOOGLE_STORAGE_PATH", default="gs://my_bucket")

def storage_path(storage_env=STORAGE_ENV):
	storage_paths = {
		"local": os.path.join(os.path.dirname(__file__), "..", "model"),
		"remote": GOOGLE_STORAGE_PATH
	}
	return storage_paths[storage_env]

def weights_filepath(storage_env=STORAGE_ENV):
	return os.path.join(storage_path(storage_env), "weights", "final_weights.hdf5")

def dictionaries_dirpath(storage_env=STORAGE_ENV):
	return os.path.join(storage_path(storage_env), "dictionaries")

def my_buckets():
	storage_client = storage.Client()
	buckets = list(storage_client.list_buckets())
	return buckets

if __name__ == "__main__":

	for bucket in my_buckets():
		print(bucket)

	remote_filepaths = [
		weights_filepath("remote"),
		os.path.join(dictionaries_dirpath("remote"), "dic.txt"),
		os.path.join(dictionaries_dirpath("remote"), "dic_s.txt"),
		os.path.join(storage_path("remote"), "gradebook.csv"),
	]
	import tensorflow as tf
	for filepath in remote_filepaths:
		print(filepath, tf.io.gfile.exists(filepath))
