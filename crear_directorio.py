import boto3

def lambda_handler(event, context):
    bucket = event["body"]["bucket"]
    directorio = event["body"]["directorio"]
    s3 = boto3.client("s3")
    try:
        s3.put_object(
            Bucket=bucket,
            Key=(directorio + "/")
        )
        message = "Bucket" + str(directorio) + " creado con éxito"
        return {
            'statusCode': 201,
            'message': message
        }
    except Exception as e:
        return {
            "statusCode": 400,
            "message":"No se pudo crear el directorio",
            "error": str(e)
        }