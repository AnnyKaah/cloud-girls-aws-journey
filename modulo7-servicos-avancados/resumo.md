# Módulo 7 – Serviços Intermediários e Avançados

## Resumo
Neste módulo, aprofundamos serviços intermediários e avançados da AWS, incluindo **Lambda avançado**, **ECS**, **EKS**, **SNS** e **SQS**. O foco é entender **orquestração de containers**, **serverless avançado** e **comunicação assíncrona** entre sistemas.

---

## AWS Lambda Avançado

- **O que é**: Execução de código serverless, escalável automaticamente.  
- **Conceitos avançados**:
  - Triggers de eventos (S3, DynamoDB, API Gateway)  
  - Variáveis de ambiente para configuração  
  - Funções assíncronas e timeout configurável  
- **Exemplo prático**: Lambda que processa arquivos enviados para S3 e envia notificação via SNS

---

## Amazon ECS e EKS – Orquestração de Containers

- **ECS (Elastic Container Service)**: Serviço gerenciado para executar containers Docker.  
- **EKS (Elastic Kubernetes Service)**: Kubernetes totalmente gerenciado na AWS.  
- **Diferenças ECS vs EKS**:
  - ECS: mais simples, integração nativa com AWS  
  - EKS: mais flexível, compatível com Kubernetes padrão  
- **Exemplo prático**: Deploy de uma aplicação web em ECS com 2 containers e balanceamento via ALB

---

## Amazon SNS e SQS – Comunicação Assíncrona

- **SNS (Simple Notification Service)**:
  - Serviço de pub/sub para enviar notificações em tempo real  
  - Exemplo: Enviar email ou SMS quando um arquivo é enviado ao S3
- **SQS (Simple Queue Service)**:
  - Fila de mensagens para desacoplar aplicações  
  - Exemplo: Colocar pedidos de processamento em fila para Lambda consumir

---

## Diagrama ECS + ALB

> Explicação: Usuários chegam pelo Application Load Balancer (ALB); o ALB encaminha para o target group do serviço ECS (tasks/container instances). O serviço ECS escala tasks e envia logs/metrics para CloudWatch.

```mermaid
graph TD
    A[Usuario] --> B[Application Load Balancer ALB]
    B --> TG[Target Group]
    TG --> S[ECS Service Tasks]
    S --> T[ECS Task Container]
    S --> CW[CloudWatch Metrics Logs]

    style A fill:#FF9900,stroke:#333,stroke-width:2px
    style B fill:#4A90E2,color:#FFF
    style TG fill:#FFD700,color:#000
    style S fill:#232F3E,stroke:#F90,stroke-width:2px,color:#FFF
    style T fill:#232F3E,stroke:#F90,stroke-width:2px,color:#FFF
    style CW fill:#9013FE,color:#FFF
```

## Diagrama Kubernetes + Ingress/ALB

> Explicação: Usuários chegam pelo Ingress (ou ALB equivalente); o Ingress encaminha para o Kubernetes Service, que gerencia Pods (via Deployment/ReplicaSet). Pods usam ConfigMaps/Secrets e enviam métricas para CloudWatch.

```mermaid
graph TD
    U[Usuario] --> I[Ingress ALB]
    I --> Svc[Kubernetes Service]
    Svc --> P[Pods Deployment ReplicaSet]
    P --> CM[ConfigMap Secret]
    P --> M[Metrics CloudWatch Prometheus]

    style U fill:#FF9900,stroke:#333,stroke-width:2px
    style I fill:#4A90E2,color:#FFF
    style Svc fill:#FFD700,color:#000
    style P fill:#232F3E,stroke:#F90,stroke-width:2px,color:#FFF
    style CM fill:#9013FE,color:#FFF
    style M fill:#9013FE,color:#FFF
```

## Diagrama S3 -> SNS -> Lambda -> S3 (Processamento de upload)

> Explicação: Usuário sube um arquivo no S3; S3 emite um evento para um SNS Topic (ou SNS via Event Notification); o SNS notifica uma Lambda (assinatura); a Lambda processa o arquivo e grava resultado em outro S3 (ou mesma bucket/prefix). Logs vão para CloudWatch.

```mermaid
graph TD
    U[Usuario] --> S3a[S3 Bucket Upload]
    S3a --> SNS[SNS Topic Event Notification]
    SNS --> L[Lambda Processa Evento]
    L --> S3b[S3 Bucket Resultado Processado]
    L --> CW[CloudWatch Logs]

    style U fill:#FF9900,stroke:#333,stroke-width:2px
    style S3a fill:#FFD700,color:#000
    style SNS fill:#4A90E2,color:#FFF
    style L fill:#4A90E2,color:#FFF
    style S3b fill:#FFD700,color:#000
    style CW fill:#9013FE,color:#FFF
```

## Diagrama SNS -> SQS (fanout / desacoplamento)

> Explicação: Um produtor publica mensagens em um SNS Topic; o SNS encaminha (fan-out) para uma ou mais SQS queues (subscriptions). Consumidores/workers leem da SQS de forma assíncrona. Incluí uma Dead-Letter Queue (DLQ) para mensagens que falham repetidamente.

```mermaid
graph TD
    P[Publisher App] --> SNS[SNS Topic]
    SNS --> Q1[SQS Queue Worker A]
    SNS --> Q2[SQS Queue Worker B]
    Q1 --> WorkerA[Worker A Consumer]
    Q2 --> WorkerB[Worker B Consumer]
    Q1 -.-> DLQ[Dead-Letter Queue Falhas]
    Q2 -.-> DLQ

    style P fill:#FF9900,stroke:#333,stroke-width:2px
    style SNS fill:#4A90E2,color:#FFF
    style Q1 fill:#FFD700,color:#000
    style Q2 fill:#FFD700,color:#000
    style WorkerA fill:#232F3E,stroke:#F90,stroke-width:2px,color:#FFF
    style WorkerB fill:#232F3E,stroke:#F90,stroke-width:2px,color:#FFF
    style DLQ fill:#9013FE,color:#FFF
```
---

## 🎯 Dicas importantes

- Usar Lambda para tarefas event-driven e processamento serverless  
- ECS para aplicações containerizadas que precisam de gerenciamento simplificado  
- EKS quando já se domina Kubernetes ou precisa de portabilidade  
- SNS + SQS garantem comunicação confiável e escalável entre sistemas

