#############################################################################
#
# Copy and Paste this code in AWS LAMBDA and Give Necessary role permissions 
# 
# This Code is not for outside AWS
#
##############################################################################




import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # List all snapshots
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']
    
    for snapshot in snapshots:
        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot['VolumeId']
        
        # Describe the volume
        try:
            volume = ec2.describe_volumes(VolumeIds=[volume_id])['Volumes'][0]
            state = volume['State']
            attachments = volume['Attachments']
            
            # Check if the volume is either deleted or available and not attached to any EC2 instance
            if state == 'available' and not attachments:
                print(f"Deleting snapshot {snapshot_id} for available volume {volume_id} with no attachments.")
                ec2.delete_snapshot(SnapshotId=snapshot_id)
            elif state == 'deleted':
                print(f"Deleting snapshot {snapshot_id} for deleted volume {volume_id}.")
                ec2.delete_snapshot(SnapshotId=snapshot_id)
                
        except ec2.exceptions.ClientError as e:
            if 'InvalidVolume.NotFound' in str(e):
                print(f"Volume {volume_id} not found (probably already deleted). Deleting snapshot {snapshot_id}.")
                ec2.delete_snapshot(SnapshotId=snapshot_id)
            else:
                print(f"Unexpected error when describing volume {volume_id}: {e}")
                
    return {
        'statusCode': 200,
        'body': 'Completed snapshot cleanup.'
    }
