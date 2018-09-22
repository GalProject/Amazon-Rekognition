import boto3
import json
import collections import defaultdict

s3 = boto3.resource('s3')
my_bucket = s3.Bucket('bucket-gal3')
client = boto3.client('rekognition','us-east-1')

dict_of_images = defaultdict(list)

def DetectLabelsInImage(image,dict_of_images):
    response = client.detect_labels(Image={'S3Object':{'Bucket':image.bucket_name,'Name':image.key}})
    for lables in response['Labels']:
        if (labels['Confidence'] > 90.0):
            dict_of_images[labels['Name']].appent(image.key)


for obj in my_bucket.objects.all():
    DetectLabelsInImage(obj,dict_of_images)

with open('processed_images_file.json','w') as image:
    json.dump(dict_of_images,image)
