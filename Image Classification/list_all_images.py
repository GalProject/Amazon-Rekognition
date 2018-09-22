# in this script, we will connect to our S3 bucket and list all the images
# boto3 - .....
# s3 - to work with S3 objects
# my_bucket - the bucket name

import boto3

s3 = boto3.resource('s3')
my_bucket = s3.Bucket('bucket-gal3')

for obj in my_bucket.objects.all():
    print(str(obj.key))
