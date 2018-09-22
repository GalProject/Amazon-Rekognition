# this is an example of Amazon Rekognition - detect text from an image
# filename - the image name inisde my S3 bucket
# my_bucket - the name of my S3 Bucket
# boto3 - to connect Amazon Rekognition API
# json - to make it human readable
# client - rekognition its the service, us-east-1 its the region
# response - the response is python dictionary
# jsonRes - convert response to json file

import boto3
import json

my_image_name = 'car_plate.jpg'
my_bucket = 'bucket-gal2'

client = boto3.client('rekognition','us-east-1')

response = client.detect_text(Image={'S3Object':{'Bucket':my_bucket,'Name':my_image_name}})

jsonRes = json.dump(response,indent=2)

print(jsonRes)
