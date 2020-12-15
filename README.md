

https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-UsingHTTPPOST.html

Voorbeeld code voor pre-signed url: https://github.com/codingjoe/django-s3file/blob/9b751fb01640491c9d1fb81117dfd0b7f36188cf/s3file/forms.py#L56

Boto3 heeft een generate_presigned_post en _url functie.
Flask app die boto3.client('s3').generate_presigned_post(..) gebruikt
(ipv generate_presigned_url)

Mooie uitleg voor _post vs _url methods: https://stackoverflow.com/questions/65198959/aws-s3-generate-presigned-url-vs-generate-presigned-post-for-uploading-files

En een prachtig voorbeeld in een flask app's html: https://github.com/willwebberley/FlaskDirectUploader/blob/master/templates/account.html

En een capabel react component: https://www.npmjs.com/package/react-s3-uploader



```
poetry install
poetry shell
uvicorn server:app --reload
```
