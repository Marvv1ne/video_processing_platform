from fastapi import UploadFile
import boto3
from botocore.exceptions import ClientError
from botocore.config import Config

from backend.app.core.settings import settings


class S3Client:
    def __init__(
        self,
        access_key: str,
        secret_key: str,
        endpoint_url: str,
        bucket_name: str,
    ):
        config = Config(
            signature_version="s3v4",
            s3={"address_style": "path"},
        )
        self.client = boto3.client(
            "s3",
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            endpoint_url=endpoint_url,
            config=config,
            use_ssl=False,
            verify=False,
        )
        self.bucket_name = bucket_name

    def upload_file(self, file: UploadFile) -> dict:
        file.file.seek(0)
        self.client.put_object(
            Bucket=self.bucket_name,
            Key=file.filename,
            Body=file.file,
        )
        return {"message": "sucsess"}


s3_client = S3Client(
    access_key=settings.s3.access_key,
    secret_key=settings.s3.secret_key,
    endpoint_url=settings.s3.endpoint_url,
    bucket_name=settings.s3.bucket_name,
)
