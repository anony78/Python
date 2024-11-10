import boto3

aws_management_console = boto3.session.Session(profile_name = "gedorica")
# OPen EC2 Console
ec2_console = aws_managament_console.client(service_name = "ec2")
response = ec2_console.stop_instances(
    InstanceIds=[
        'i-085d2bade2fbef260'
    ],
)