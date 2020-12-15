import base64
import datetime
import json
import os
from typing import Optional
import boto3
import hmac

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

class FakeDjangoSettings:
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    SECRET_KEY = os.environ['SECRET_KEY']

settings = FakeDjangoSettings()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

@app.get("/get_signed_url")
def signed_url_endpoint():
    return signing_code('wakanda4ever', 'foobar.pdf')

def signing_code(bucket_name, key, **policy):
    # Step 1. Base64 encoded security policy (StringToSign)
    policy = json.dumps(policy).encode()
    policy_b64 = base64.b64encode(policy).decode()

    date = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    aws_id = getattr(
        settings,
        "AWS_ACCESS_KEY_ID",
        "AWS_ACCESS_KEY_ID",
    )
    fields = {
        "x-amz-algorithm": "AWS4-HMAC-SHA256",
        "x-amz-date": date,
        "x-amz-credential": aws_id,
        "policy": policy_b64,
        "key": key,
    }
    # Step 3. Signature
    signature = hmac.new(
        settings.SECRET_KEY.encode(),
        policy + date.encode(),
        "sha256",
    ).digest()
    signature = base64.b64encode(signature).decode()
    return {
        "url": "/__s3_mock__/",
        "fields": {"x-amz-signature": signature, **fields},
    }

app.mount("/", StaticFiles(directory="static", html=True), name="static")
