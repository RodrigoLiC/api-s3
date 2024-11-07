import boto3

def lambda_handler(event, context):
    nombre_bucket = event["body"]["name"]
    try:
        s3 = boto3.client("s3")
        s3.create_bucket(Bucket=nombre_bucket, ObjectOwnership="BucketOwnerPreferred")
        s3.put_public_access_block(Bucket=nombre_bucket, PublicAccessBlockConfiguration={'BlockPublicAcls': False,'IgnorePublicAcls': False,'BlockPublicPolicy': False,'RestrictPublicBuckets': False})
        s3.put_bucket_acl(ACL='public-read-write',Bucket=nombre_bucket)
        message = "Bucket" + str(nombre_bucket) + " creado con éxito"
        return {
            "statusCode":201,
            "message": message,
        }
    except Exception as e:
        return {
            "statusCode": 400,
            "message":"No se pudo crear el bucket",
            "error": str(e)
        }