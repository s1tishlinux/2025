import json
import boto3

def lambda_handler(event, context):
    """Process S3 events and copy files to another bucket"""
    
    s3_client = boto3.client('s3')
    
    try:
        # Get bucket and file details from event
        source_bucket = event['Records'][0]['s3']['bucket']['name']
        file_name = event['Records'][0]['s3']['object']['key']
        target_bucket = 'XXXXXXXXXXXXXXXXXXXXXXX'
        
        # Copy file to target bucket
        copy_source = {'Bucket': source_bucket, 'Key': file_name}
        s3_client.copy_object(
            CopySource=copy_source,
            Bucket=target_bucket,
            Key=file_name
        )
        
        
        return {
            'statusCode': 200,
            'body': json.dumps(f'File {file_name} copied successfully')
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
