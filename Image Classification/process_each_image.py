import boto3

s3 = boto3.resource('s3')
my_bucket = s3.Bucket('bucket-gal3')
client = boto3.client('rekognition','us-east-1')

def DetectLabelsInImage(image):
    response = client.detect_labels(Image={'S3Object':{'Bucket':image.bucket_name,'Name':image.key}})
    for lables in response['Labels']:
        print(labels) #Result - Lable + Confidence - (Car,92.4444)


for obj in my_bucket.objects.all():
    DetectLabelsInImage(obj)
