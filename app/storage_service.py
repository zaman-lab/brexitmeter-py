
import os
from dotenv import load_dotenv

from google.cloud import storage

from app.model import unweighted_model

load_dotenv()

MODEL_WEIGHTS_FILEPATH = os.getenv("MODEL_WEIGHTS_FILEPATH", default="gs://OOPS.hd5")

def my_buckets():
    storage_client = storage.Client()
    buckets = list(storage_client.list_buckets())
    print(buckets)











from app.helper_text import main_clean

def compute_polarity(txt, model):
	"""
	Params:
		txt is the text to classify
		model is the model used to perform the classification
	"""
	x, x_s = main_clean(txt)

	result = model.predict([x, x_s])

	return result


if __name__ == "__main__":

	# https://github.com/keras-team/keras/pull/11636/files#diff-2c1a7aa0055f88618fd60251c8be9e7bR377-R405

	model = unweighted_model()

	import tensorflow as tf
	tf.io.gfile.exists(MODEL_WEIGHTS_FILEPATH)

	print(MODEL_WEIGHTS_FILEPATH)
	weighted_model = model.load_weights(MODEL_WEIGHTS_FILEPATH)
	#> All attempts to get a Google authentication bearer token failed, returning an empty token. Retrieving token from files failed with "Not found: Could not locate the credentials file.". Retrieving token from GCE failed with "Aborted: All 10 retry attempts failed. The last failure: Unavailable: Error executing an HTTP request: libcurl code 6 meaning 'Couldn't resolve host name', error details: Couldn't resolve host 'metadata'"

	breakpoint()
	result = compute_polarity(user_text, model)

	polarity_pro = result[:,1] # or result[0][1]

	print(f"This text is {polarity_pro} Pro Brexit")
