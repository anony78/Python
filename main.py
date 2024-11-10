# creating EC2 instance

import boto3

# Set up EC2 client

ec2= boto3.ec2('ec2')

# Specify instance parameters
image_id ='ami-09007aa1ef7d7fc1f'
instance_type ='t2.micro'
key_name ='Wordpress'
security_group_ids='sg-0e3bee1c4fa64a404'
subnet_id ='subnet-0788b3ff731141666'


response = ec2.run_instances(ImadeId=image_id, InstanceType= instance_type, key_name=key_name, MaxCount=1)

instance_id = response['Instances'][0]['InstanceID']





