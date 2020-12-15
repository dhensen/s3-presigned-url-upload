import mimetypes
import os

import boto3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

S3_BUCKET = os.environ['S3_BUCKET']

boto3_session = boto3.Session(
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
    region_name=os.environ['AWS_REGION'])

s3 = boto3_session.client('s3')


@app.get("/s3/sign")
def sign_s3_upload(objectName: str):
    mime_type, _ = mimetypes.guess_type(objectName)
    presigned_url = s3.generate_presigned_url(
        'put_object',
        Params={
            'Bucket': S3_BUCKET,
            'Key': objectName,
            'ContentType': mime_type,
            'ACL': 'public-read',
        },
        ExpiresIn=3600,
    )

    return {'signedUrl': presigned_url}


app.mount("/",
          StaticFiles(directory="upload-frontend/build", html=True),
          name="static")
