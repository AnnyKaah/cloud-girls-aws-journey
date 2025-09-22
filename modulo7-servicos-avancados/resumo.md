# Módulo 7 – Serviços Intermediários e Avançados

## 📌 Resumo
Neste módulo, aprofundamos serviços intermediários e avançados da AWS, incluindo **Lambda avançado**, **ECS**, **EKS**, **SNS** e **SQS**. O foco é entender **orquestração de containers**, **serverless avançado** e **comunicação assíncrona** entre sistemas.

---

## 🌀 AWS Lambda Avançado

- **O que é**: Execução de código serverless, escalável automaticamente.  
- **Conceitos avançados**:
  - Triggers de eventos (S3, DynamoDB, API Gateway)  
  - Variáveis de ambiente para configuração  
  - Funções assíncronas e timeout configurável  
- **Exemplo prático**: Lambda que processa arquivos enviados para S3 e envia notificação via SNS

---

## 📦 Amazon ECS e EKS – Orquestração de Containers

- **ECS (Elastic Container Service)**: Serviço gerenciado para executar containers Docker.  
- **EKS (Elastic Kubernetes Service)**: Kubernetes totalmente gerenciado na AWS.  
- **Diferenças ECS vs EKS**:
  - ECS: mais simples, integração nativa com AWS  
  - EKS: mais flexível, compatível com Kubernetes padrão  
- **Exemplo prático**: Deploy de uma aplicação web em ECS com 2 containers e balanceamento via ALB

---

## 🔔 Amazon SNS e SQS – Comunicação Assíncrona

- **SNS (Simple Notification Service)**:
  - Serviço de pub/sub para enviar notificações em tempo real  
  - Exemplo: Enviar email ou SMS quando um arquivo é enviado ao S3
- **SQS (Simple Queue Service)**:
  - Fila de mensagens para desacoplar aplicações  
  - Exemplo: Colocar pedidos de processamento em fila para Lambda consumir

---

## 🎯 Dicas importantes

- Usar Lambda para tarefas event-driven e processamento serverless  
- ECS para aplicações containerizadas que precisam de gerenciamento simplificado  
- EKS quando já se domina Kubernetes ou precisa de portabilidade  
- SNS + SQS garantem comunicação confiável e escalável entre sistemas
