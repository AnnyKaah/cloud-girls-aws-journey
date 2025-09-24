import json
import boto3

def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        
        print(f"Arquivo recebido: {key} no bucket {bucket}")
        # Exemplo: copiar arquivo para outro bucket
        s3_client.copy_object(
            Bucket='meu-bucket-destino',
            CopySource={'Bucket': bucket, 'Key': key},
            Key=key
        )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Processamento concluído!')
    }
