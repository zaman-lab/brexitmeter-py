
import os
from dotenv import load_dotenv

from app.model import unweighted_model

load_dotenv()

GCS_MODEL_WEIGHTS_FILEPATH = os.getenv("GCS_MODEL_WEIGHTS_FILEPATH", default="gs://OOPS.hd5")

if __name__ == "__main__":

	# https://github.com/keras-team/keras/pull/11636/files#diff-2c1a7aa0055f88618fd60251c8be9e7bR377-R405

	model = unweighted_model()

	print(GCS_MODEL_WEIGHTS_FILEPATH)
	weighted_model = model.load_weights(GCS_MODEL_WEIGHTS_FILEPATH)
	#> All attempts to get a Google authentication bearer token failed, returning an empty token. Retrieving token from files failed with "Not found: Could not locate the credentials file.". Retrieving token from GCE failed with "Aborted: All 10 retry attempts failed. The last failure: Unavailable: Error executing an HTTP request: libcurl code 6 meaning 'Couldn't resolve host name', error details: Couldn't resolve host 'metadata'"
	breakpoint()

	#model.load_weights(file_contents) #> OSError
