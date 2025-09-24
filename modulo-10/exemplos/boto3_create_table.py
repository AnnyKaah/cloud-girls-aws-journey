import boto3

# Conectar ao DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Criar tabela
table = dynamodb.create_table(
    TableName='MinhaTabela',
    KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
    AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
    ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
)

print("Tabela criada com sucesso!")
