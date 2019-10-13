

import os
from dotenv import load_dotenv
from google.cloud import storage

load_dotenv()

STORAGE_ENV = os.getenv("STORAGE_ENV", default="local") # "local" OR "remote"
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", default="OOPS") # implicit check by google.cloud (and keras)
GOOGLE_STORAGE_BUCKET_PATH=os.getenv("GOOGLE_STORAGE_BUCKET_PATH", default="gs://oops")

# os.getenv("REMOTE_DICTIONARIES_DIRPATH", default="gs://my_bucket/dictionaries/")
# os.path.join(os.path.dirname(__file__), "..", "dictionaries")
# os.path.join(os.path.dirname(__file__), "..", "model", "final_weights.hdf5")

def weights_filepath(storage_env=STORAGE_ENV):
	if storage_env == "remote":
		filepath = os.path.join(, default="gs://my_bucket/weights/final_weights.hd5")
	elif storage_env =="local":
		filepath = os.getenv("REMOTE_WEIGHTS_FILEPATH", default="gs://my_bucket/weights/final_weights.hd5")

	return filepath

def dictionaries_dirpath(storage_env=STORAGE_ENV):
	pass

def my_buckets():
    storage_client = storage.Client()
    buckets = list(storage_client.list_buckets())
	return buckets

if __name__ == "__main__":

	for bucket in my_buckets():
		print(bucket)

	import tensorflow as tf
	tf.io.gfile.exists(REMOTE_WEIGHTS_FILEPATH)
	tf.io.gfile.exists(os.path.join(REMOTE_WEIGHTS_FILEPATH, "dic.txt"))
	tf.io.gfile.exists(os.path.join(REMOTE_WEIGHTS_FILEPATH, "dic.txt"))
	tf.io.gfile.exists(os.path.join(REMOTE_WEIGHTS_FILEPATH, "dic.txt"))

	# todo: read gradebook.csv file with pandas
