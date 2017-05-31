import boto3
session = boto3.Session(profile_name='iMinjar')
iam = boto3.client('iam')
response = iam.list_users()
for user in response:
	print response.Users.UserName
'''paginator = iam.get_paginator('list_access_keys')
for response in paginator.paginate(UserName='IAM_USER_NAME'):
#print paginator[3:]
	print(response)'''