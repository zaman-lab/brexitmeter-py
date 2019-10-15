

import os
from dotenv import load_dotenv
from google.cloud import storage
import tensorflow as tf # from tensorflow.io import gfile

load_dotenv()

STORAGE_ENV = os.getenv("STORAGE_ENV", default="local") # "local" OR "remote"
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", default="OOPS") # implicit check by google.cloud (and keras)
GOOGLE_STORAGE_PATH=os.getenv("GOOGLE_STORAGE_PATH", default="gs://brexitmeter-bucket")

def storage_path(storage_env=STORAGE_ENV):
	storage_paths = {
		"local": os.path.join(os.path.dirname(__file__), "..", "model"),
		"remote": GOOGLE_STORAGE_PATH
	}
	return storage_paths[storage_env]

def weights_filepath(storage_env=STORAGE_ENV):
	return os.path.join(storage_path(storage_env), "weights", "final_weights.hdf5")

def dictionaries_dirpath(storage_env=STORAGE_ENV):
	return os.path.join(storage_path("local"), "dictionaries")

def my_buckets():
	storage_client = storage.Client()
	buckets = list(storage_client.list_buckets())
	return buckets

if __name__ == "__main__":

	if STORAGE_ENV == "remote":
		print("------------")
		print("MY BUCKETS:")
		for bucket in my_buckets():
			print(bucket)

	print("------------")
	print(f"{STORAGE_ENV.upper()} MODEL FILES:")
	model_filepaths = [
		weights_filepath(STORAGE_ENV),
		os.path.join(dictionaries_dirpath(STORAGE_ENV), "dic.txt"),
		os.path.join(dictionaries_dirpath(STORAGE_ENV), "dic_s.txt"),
	]
	for filepath in model_filepaths:
		print(os.path.abspath(filepath), tf.io.gfile.exists(filepath))
