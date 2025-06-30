import boto3

s3 = boto3.client(
    's3',
    aws_access_key_id='AKIA47CR3RDBACHENTXX',
    aws_secret_access_key='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'
)

bucket_name = 'generate-qr-vprofile'

try:
    # Test access by listing objects in the bucket
    response = s3.list_objects_v2(Bucket=bucket_name)
    print("Objects in bucket:", response.get('Contents', []))
except Exception as e:
    print("Error:", e)
    