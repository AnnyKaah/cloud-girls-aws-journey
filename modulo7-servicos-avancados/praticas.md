# Módulo 7 – Práticas e Exercícios

## 🚀 Hands-on realizados

1. **Lambda Avançado**
   - Criar função Lambda: `processa_s3_event`  
   - Trigger: upload de arquivo no bucket S3  
   - Código Python:
     ```python
     import boto3

     sns = boto3.client('sns')
     def lambda_handler(event, context):
         bucket = event['Records'][0]['s3']['bucket']['name']
         arquivo = event['Records'][0]['s3']['object']['key']
         sns.publish(
             TopicArn='arn:aws:sns:REGIAO:ID:MeuTopico',
             Message=f'Arquivo {arquivo} enviado para {bucket}'
         )
         return 'Mensagem enviada'
     ```
   - Testar upload de arquivo no S3  

2. **Deploy em ECS**
   - Criar cluster ECS  
   - Criar task definition com 2 containers (ex.: backend e frontend)  
   - Deploy em cluster e verificar health check no ALB  

3. **Explorando EKS**
   - Criar cluster EKS via console ou CLI  
   - Deploy simples de pod com Nginx  
   - Verificar status com `kubectl get pods`  

4. **SNS e SQS**
   - Criar tópico SNS: `notificacoes`  
   - Criar fila SQS: `fila-processamento`  
   - Configurar Lambda para consumir mensagens da fila  
   - Testar envio e processamento assíncrono

## 📝 Observações

- Lambda + S3 + SNS é padrão serverless para pipelines simples  
- ECS simplifica deploy de containers sem Kubernetes  
- EKS oferece flexibilidade e compatibilidade, mas exige mais configuração  
- SNS + SQS ajudam a desacoplar serviços, aumentando escalabilidade e tolerância a falhas  

## 📂 Imagens e Diagramas

- [Diagrama Lambda + SNS + S3](diagramas/lambda-sns-s3.webp)  
- [Diagrama ECS + ALB](diagramas/ecs-alb.png)  
- [Diagrama EKS simples](diagramas/eks-pods.png)  
- [Diagrama SNS + SQS](diagramas/sns-sqs.png)
