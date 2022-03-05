import os
import boto3

ec2 = boto3.resource('ec2')
name = os.getenv('Name')

def lambda_handler(event, context):
    filters = [
        {
            'Name': 'tag:Name',
            'Values': [name]
        },
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }]

    instances = ec2.instances.filter(Filters=filters)

    runningInstances = [instance.id for instance in instances]

    if len(runningInstances) > 0:
        startingUp = ec2.instances.filter(InstanceIds=runningInstances).stop()
        print(f"Stopping {len(runningInstances)} {name} instances with id - {runningInstances}")
    else:
        print(f"There are no instances that are runing with name {name}")
