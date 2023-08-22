import boto3
# change the region name below 
region = 'us-east-1'
#change the Instance ID 
instances = ['i-064369a69363fa9f7',]
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))