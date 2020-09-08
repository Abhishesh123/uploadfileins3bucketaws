import boto3
import os 

def key_exists(mykey, mybucket):
	ACCESS_KEY = 'xxxxxxxxxxxxxxxx'
	SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
	
	s3_client = boto3.client('s3',aws_access_key_id=ACCESS_KEY,
                        aws_secret_access_key=SECRET_KEY,
                        region_name='ap-south-1')
	response = s3_client.list_objects_v2(Bucket=mybucket, Prefix=mykey)
	# print(response)
	if response:
		try:
			contents = response['Contents']
		except KeyError:
			return 
		for obj in contents:
			print(obj['Key'])
			print(mykey)
			if mykey == obj['Key']:
				return True
		return False

for file in os.listdir('media/'):
	file_name = 'media/'+file
	print(file_name)
	if key_exists(file_name,'production-bucket'):
		print("key exists")
	else:
		print("safe to put new bucket object")