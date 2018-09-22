# this example is working on Cloud9 Console
# S3 Object - you need to create you Bucket on S3
# Bucket - the name of the bucket
# Name - the name of the image
# Region - insert the closest region to your server
aws rekognition detect-labels --image "{\"S3Object\":{\"Bucket\":\"bucket-gal2\",\"Name\":\"car.jpg\"}}" --region us-east-1 > image_detect_labels_result
