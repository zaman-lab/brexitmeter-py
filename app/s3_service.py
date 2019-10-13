import os
from dotenv import load_dotenv
import boto3

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

	#import pandas
	breakpoint()


	#df = pandas.read_csv(file_contents)
