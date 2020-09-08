import boto3
import os 

def key_exists(mykey, mybucket):
	ACCESS_KEY = 'xxxxxxxxxxxxxxxxxx'
	SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
	
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
		base_path = 'media/'
		# counter = 0
		for file in os.listdir(base_path):
			print(file)
			file_name = base_path+'/'+file
			ACCESS_KEY = 'xxxxxxxxxxxxxx'
			SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
			s3_client = boto3.client('s3',aws_access_key_id=ACCESS_KEY,
                        aws_secret_access_key=SECRET_KEY,
                        region_name='ap-south-1')
			s3_client.upload_file(file_name, 'production-bucket', 'media/{}'.format(file))
			print("successfully uploaded ")

    