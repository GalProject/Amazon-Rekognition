import json
import sys

s3 = boto3.resource('s3')
my_bucket = s3.Bucket('bucket-gal3')
client = boto3.client('rekognition','us-east-1')

if (len(sys.argv) == 1):
    print('error: please enter keywords after the script')
    exit()

with open('processed_images_file.json','w') as file:
    data = json.load(file)
    for i in range(1,len(sys.argv)):
        keyword = sys.argv[i]
        print('This is the Keyword' + str(keyword))
        for j in data[keyword]:
            print j
