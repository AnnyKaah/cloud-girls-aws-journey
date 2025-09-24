# Módulo 5 – Bancos de Dados na AWS

## 📌 Resumo
Neste módulo, aprendemos sobre **Amazon RDS**, **DynamoDB** e estratégias de **backup e recuperação de dados**. Entender bancos de dados na nuvem é essencial para criar aplicações confiáveis, escaláveis e seguras.

---

## 🗄️ Amazon RDS (Relational Database Service)

- **O que é RDS**: Banco de dados relacional totalmente gerenciado pela AWS.  
- **Benefícios**:  
  - Automação de backups e atualizações  
  - Alta disponibilidade com Multi-AZ  
  - Escalabilidade de armazenamento e computação  
- **Exemplo de uso**: MySQL, PostgreSQL ou SQL Server para aplicação web.  

---

## 🌐 Amazon DynamoDB

- **O que é DynamoDB**: Banco de dados NoSQL totalmente gerenciado, de alta performance e escalabilidade automática.  
- **Características**:  
  - Chave-valor e documentos  
  - Latência baixa e previsível  
  - Backup e restore automáticos  
- **Exemplo de uso**: Armazenamento de sessões de usuários ou dados de IoT em tempo real.  

---

## 💾 Estratégias de Backup e Recuperação de Dados

- **Backup**: Processo de salvar cópias dos dados para recuperação futura.  
- **Recuperação**: Restaurar dados em caso de falha, perda ou corrupção.  
- **Práticas recomendadas na AWS**:
  - Habilitar **automated backups** no RDS  
  - Criar **snapshots manuais** antes de atualizações críticas  
  - Utilizar **versionamento e replicação** no S3 e DynamoDB  
- **Exemplo prático**: Criar snapshot de RDS antes de atualizar instância e restaurar em caso de erro.

---

## 🎯 Dicas importantes

- Escolher **RDS para dados relacionais** e **DynamoDB para NoSQL**  
- Garantir que backups estejam em **outra região** para recuperação em desastres  
- Monitorar métricas com **CloudWatch** para antecipar problemas

## Backup e Restore (S3 e RDS)

> ✅ Explicação: A aplicação envia dados → backup automático → armazenamento durável → restauração → retorna para o banco/S3.

```mermaid
graph TD
    A[💻 Aplicação / Usuário] --> B[📁 S3 Bucket / 💾 RDS Database]
    B --> C[🗂 Backup Automático]
    C --> D[📦 Armazenamento Durável - Glacier / Backup RDS]
    D --> E[🔄 Restore Disponível]
    E --> B

    style A fill:#232F3E,stroke:#F90,stroke-width:2px,color:#FFF
    style B fill:#FFD700,color:#000
    style C fill:#4A90E2,color:#FFF
    style D fill:#9013FE,color:#FFF
    style E fill:#00FF00,stroke:#333,stroke-width:2px

```

---

## DynamoDB Table

> ✅ Explicação: Fluxo de dados e eventos: app escreve/consulta → DynamoDB → eventos disparam Lambda → logs monitorados no CloudWatch.

```mermaid
graph TD
    A[💻 Aplicacao / Usuario] --> B[📋 DynamoDB Table]
    B --> C[⚡ Lambda Function - Event Trigger]
    C --> D[📊 CloudWatch Logs]
    B --> D

    style A fill:#232F3E,stroke:#F90,stroke-width:2px,color:#FFF
    style B fill:#FFD700,color:#000
    style C fill:#4A90E2,color:#FFF
    style D fill:#9013FE,color:#FFF
```

---

## RDS Dashboard

> ✅ Explicação: Métricas e logs vão para o CloudWatch, que alimenta dashboards e aciona alarmes e notificações, refletindo melhor o monitoramento RDS.
> 
```mermaid
graph TD
    A[💾 RDS Database] --> B[📊 CloudWatch Metrics]
    A --> C[📋 CloudWatch Logs]
    B --> D[📈 Dashboard Personalizado]
    C --> D
    D --> E[🚨 Alarmes - Thresholds]
    E --> F[🔔 Notificacoes / Acoes Automatizadas]

    style A fill:#FFD700,color:#000
    style B fill:#4A90E2,color:#FFF
    style C fill:#9013FE,color:#FFF
    style D fill:#FF9900,color:#000
    style E fill:#FF9900,color:#000
    style F fill:#00FF00,stroke:#333,stroke-width:2px
```
