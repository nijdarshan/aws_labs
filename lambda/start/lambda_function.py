import boto3

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    filters = [
        {
            'Name': 'tag:Name',
            'Values': ['Lambda-ec2']
        },
        {
            'Name': 'instance-state-name',
            'Values': ['stopped']
        }]
        
    instances = ec2.instances.filter(Filters=filters)
    
    stoppedInstances = [instance.id for instance in instances]
    
    if len(stoppedInstances) > 0:
        startingUp = ec2.instances.filter(InstanceIds=stoppedInstances).start()
        print(f"Starting {len(stoppedInstances)} Lambda-ec2 instances with id - {stoppedInstances}")
    else:
        print(f"There are no instances that are stopped with name Lambda-ec2")
        
