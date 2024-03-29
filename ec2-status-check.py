import boto3    #aws library for python
import schedule

ec2_client = boto3.client('ec2', region_name='us-east-2')
ec2_resource = boto3.resource('ec2', region_name='us-east-2')



def check_instance_status():
    statuses = ec2_client.describe_instance_status(
        # IncludesAllInstances=True
    )
    for status in statuses['InstanceStatuses']:
        ins_status = status['InstanceStatus']['Status']
        sys_status = status['SystemStatus']['Status']
        state = status['InstanceState']['Name']
        print(
            f"Instance {status['InstanceId']} is {state} with instance status {ins_status} and system status {sys_status}")

schedule.every(5).seconds.do(check_instance_status)   #run the program every 5 seconds

while True:
    schedule.run_pending()




