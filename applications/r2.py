import boto3
from botocore.client import Config
from django.conf import settings


def generate_signed_url(key, expiry=300):
    client = boto3.client(
        "s3",
        endpoint_url=settings.AWS_S3_ENDPOINT_URL,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name="auto",
        config=Config(signature_version="s3v4"),
    )

    return client.generate_presigned_url(
        "get_object",
        Params={
            "Bucket": settings.AWS_STORAGE_BUCKET_NAME,
            "Key": key,
        },
        ExpiresIn=expiry,
    )
