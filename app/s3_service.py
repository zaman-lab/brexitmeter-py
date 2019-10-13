import contextlib
import os
from dotenv import load_dotenv
import boto3
import h5py

from app.model import unweighted_model

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", default="OOPS")
AWS_ACCESS_KEY_SECRET = os.getenv("AWS_ACCESS_KEY_SECRET", default="OOPS")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME", default="OOPS")
S3_MODEL_FILE_KEY = os.getenv("S3_MODEL_FILE_KEY", default="gradebook.csv")

if __name__ == "__main__":

	s3 = boto3.resource("s3")

	#buckets = list(s3.buckets.all())
	#for bucket in buckets:
	#	print("BUCKET:", bucket.name)

	csv_file = s3.Object(S3_BUCKET_NAME, S3_MODEL_FILE_KEY)
	print("FILE CONTENTS", csv_file.content_type, csv_file.content_length)

	response = csv_file.get()
	#print("RESPONSE", type(response), type(response["Body"])) #> <botocore.response.StreamingBody object

	file_contents = response["Body"].read() #> <class 'bytes'>

	model = unweighted_model()

	breakpoint()

	model.load_weights(file_contents)



	#
	# https://stackoverflow.com/a/57923863/670433
	# https://github.com/keras-team/keras/issues/9343#issuecomment-440903847
	# https://github.com/keras-team/keras/pull/11708/files
	# https://github.com/keras-team/keras/issues/9343
	# https://github.com/keras-team/keras/pull/11636
	#

	file_access_property_list = h5py.h5p.create(h5py.h5p.FILE_ACCESS)
	file_access_property_list.set_fapl_core(backing_store=False)
	file_access_property_list.set_file_image(file_contents)

	file_id_args = {
		'fapl': file_access_property_list,
		'flags': h5py.h5f.ACC_RDONLY,
		'name': b'this should never matter',
	}
	h5_file_args = {'backing_store': False, 'driver': 'core', 'mode': 'r'}

	with contextlib.closing(h5py.h5f.open(**file_id_args)) as file_id:
		with h5py.File(file_id, **h5_file_args) as h5_file:
			model.load_weights(h5_file) #> TypeError: expected str, bytes or os.PathLike object, not File

	breakpoint()
