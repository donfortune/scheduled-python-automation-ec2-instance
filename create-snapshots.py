import boto3 #python lib to interact with Aws
import schedule

client = boto3.client('ec2', region_name='us-east-2')
def automate_snapshot_creation():
    volumes = client.describe_volumes(
        Filters=[
            {
                'Name': 'tag:name',
                'Values': [
                    'prod',
                ]
            },
        ],
    )
    print(volumes['Volumes'])

    for volume in volumes['Volumes']:
        snapshots = client.create_snapshot(
            VolumeId=volume['VolumeId']
        )

        print(snapshots)

schedule.every(20).seconds.do(automate_snapshot_creation)

while True:
    schedule.run_pending()

#schedule to clean up snapshots, only need most recent snapshot

