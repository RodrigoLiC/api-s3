import base64
import boto3

def lambda_handler(event, context):
    bucket = event["body"]["bucket"]
    filename = event["body"]["filename"]
    folder = event["body"]["folder"]
    base_64_str = event["body"]["file"]

    s3 = boto3.client("s3")
    s3.put_object(Bucket=bucket, Key= folder + "/" + filename, Body=base64.b64decode(base_64_str))
    return {
        "statusCode": 201,
        "message": "Archivo subido con éxito"
    }