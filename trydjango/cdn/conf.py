import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

AWS_ACCESS_KEY_ID=os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME=os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL="https://sfo3.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
    "ACL": "public-read"
}
AWS_LOCATION = f"https://{AWS_STORAGE_BUCKET_NAME}.sfo3.digitaloceanspaces.com"

DEFAULT_FILE_STORAGE = "trydjango.cdn.backends.MediaRootS3Boto3Storage"
STATICFILES_STORAGE = "trydjango.cdn.backends.StaticRootS3Boto3Storage"