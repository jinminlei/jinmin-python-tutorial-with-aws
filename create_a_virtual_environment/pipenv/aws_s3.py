import boto3

class S3Management(object):
    def __init__(self):
        self.s3_client = boto3.client('s3')

    def get_s3_bucket_list(self):
        return self.s3_client.list_buckets()

    def get_s3_object_list(self, bucket):
        return self.s3_client.list_objects(Bucket=bucket)
