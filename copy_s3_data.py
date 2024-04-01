import boto3

def copy_s3_data(source_bucket, destination_bucket):
    s3 = boto3.client('s3')
    objects = s3.list_objects_v2(Bucket=source_bucket)['Contents']

    for obj in objects:
        key = obj['Key']
        copy_source = {'Bucket': source_bucket, 'Key': key}

        # Copy object from source bucket to destination bucket
        s3.copy_object(CopySource=copy_source, Bucket=destination_bucket, Key=key)
        print(f'Copied {key} from {source_bucket} to {destination_bucket}')

if __name__ == "__main__":
    # Replace 'source_bucket' and 'destination_bucket' with your actual bucket names
    copy_s3_data('Your-S3-Source', 'your-S3-Destination')