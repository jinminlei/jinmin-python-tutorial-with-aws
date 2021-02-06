import sys
from aws_s3 import S3Management

def run(keyword=None):
    s3 = S3Management()
    buckets = s3.get_s3_bucket_list()['Buckets']
    target_buckets = [b for b in buckets if b['Name'].find(keyword) != -1]
    result = {}
    for b in target_buckets:
        result[b['Name']] = s3.get_s3_object_list(b['Name'])['Contents']
    return result

if __name__ == '__main__':
    keyword = sys.argv[1]
    print(run(keyword=keyword))