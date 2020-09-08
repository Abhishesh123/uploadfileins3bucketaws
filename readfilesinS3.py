import boto3
import csv
import datetime

# get a handle on s3
prefix = "uploads/"
session = boto3.Session(
                    aws_access_key_id='xxxxxxxxxxxx',
                    aws_secret_access_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxx',
                    region_name='ap-south-1')
                    
s3 = session.resource('s3')

# get a handle on the bucket that holds your file
bucket = s3.Bucket('bucket-production')

# objs = [obj for obj in bucket.objects.filter(Prefix=prefix)]

# objs = [obj for obj in sorted(objs, key=get_last_modified)]
# print(objs)

FilesNotFound = True
for obj in bucket.objects.filter(Prefix=prefix):
	print('{0}:{1}:{2}'.format(bucket.name, obj.key,obj.last_modified))
	FilesNotFound = False
if FilesNotFound:
     print("ALERT", "No file in {0}/{1}".format(bucket, prefix))




 # example: energy_market_procesing
# get a handle on the object you want (i.e. your file)
# obj = bucket.Object(key='media/PostVideoImages/') # example: market/zone1/data.csv

# # get the object
# response = obj.get()
# # print(response)

# # read the contents of the file
# lines = response['Body'].read()
# print(lines)

# # saving the file data in a new file test.csv
# with open('test.csv', 'wb') as file:
#     file.write(lines)


# s3 = boto3.client('s3')
# data = s3.get_object(Bucket='my_s3_bucket', Key='main.txt')
# contents = data['Body'].read()
# print(contents)