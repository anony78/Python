#Import all the modules and the libraries
# List IAM users in AWS account
import boto3
import boto3.session
from pprint import pprint

#Open Management Console
aws_management_console = boto3.session.Session(profile_name="default")
#Open IAM console
iam_console = aws_management_console.client(service_name = "iam")
result = iam_console.list_users()
for each_user in result['Users']:
    print(each_user['UserName'])
