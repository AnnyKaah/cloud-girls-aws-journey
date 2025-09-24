# Módulo 8: Gerenciamento e Governança na AWS

**Resumo Geral**  
Este módulo foca em monitoramento, auditoria, automação de infraestrutura (IaC) e gerenciamento de acessos via IAM. Integra conceitos anteriores como CloudWatch para monitorar EC2 e CloudTrail para logs de S3/Lambda. É crucial para governança em ambientes produtivos, garantindo compliance, otimização de custos e segurança.  


---

## Seção 1: Entendendo o AWS CloudWatch

- **O que é AWS CloudWatch**: Serviço de monitoramento que coleta métricas, logs e eventos de recursos AWS.  
- **Como funciona**: Dashboards, alarmes e integração com Lambda para ações automáticas.  
- **Casos de Uso**:
  - Monitoramento de performance (ex.: latência em APIs)  
  - Geração de alertas (e-mails/SMS)  
  - Auditoria de logs serverless  

- **Logs Insights**: Consultas SQL-like em logs para análise avançada.  
- **Visualizando Logs**: Streams por serviço; filtros por timestamp, instância ou tags.  
- **Monitoramento e Validação de Dados**: Alarmes para thresholds críticos; métricas personalizadas via SDK/CLI.

**Diagrama**: [Fluxo Básico do CloudWatch](diagrams/cloudwatch.mmd)

---

## Seção 2: Fundamentos do AWS CloudTrail

- **O que é CloudTrail**: Registra todas as chamadas de API para auditoria, compliance e troubleshooting.  
- **Monitoramento de Atividades**: Management events e insights; filtragem por usuário/IP/recurso.  
- **Criando Trails**: Logs enviados a S3 ou CloudWatch; multi-região; integração com SNS.

**Diagrama**: [Integração CloudTrail e CloudWatch](diagrams/cloudtrail.mmd)

---

## Seção 3: Desafio de Projeto – CloudFormation

###Neste desafio criei minha primeira stack na AWS usando CloudFormation, incluindo recursos como EC2, S3, IAM Role e Security Group.O objetivo é praticar Infrastructure as Code (IaC) e entender como atualizar stacks de forma segura.

- **O que é CloudFormation**: IaC que usa templates JSON/YAML para provisionar recursos de forma idempotente.  
- **Arquivos do Projeto**: [Projetos CloudFormation Stack](cloud-girls-aws-journey
/desafios práticos/)

No projeto você encontrará:
- `minha-primeira-stack.yaml` – Template da stack
- `README.md` – Instruções detalhadas do desafio e passos para deploy

**Diagrama**: [Exemplo de Stack CloudFormation](diagrams/cloudformation.mmd)

---

## Seção 4: Gerenciando Usuários e Permissões (IAM)

- **IAM**: Gerencia acessos via usuários, grupos, roles e policies. Princípio de least privilege.  
- **Criação e atribuição**:
  - Criar usuário:  
    ```bash
    aws iam create-user --user-name MeuUser
    aws iam attach-user-policy --user-name MeuUser --policy-arn arn:aws:iam::aws:policy/ReadOnlyAccess
    ```
  - Configuração de credenciais: Access Key, MFA, rotação de senhas.

**Diagrama**: [Estrutura IAM](diagrams/iam.mmd)

---

## Seção 5: Policies e Roles

- Policies definem ações permitidas; roles são identities temporárias para apps/serviços.  
- Exemplo JSON Policy S3 ReadOnly: [templates/iam_policy.json]  
- Visão geral: usuários = humanos; roles = apps; auditado via CloudTrail.  
- Hands-on: trail CloudTrail + CloudWatch; stack CloudFormation com firewall; IAM user com policy restrita.

---


### **Notas e Dicas**

- Teste alarmes do CloudWatch simulando falhas.  
- Use CloudFormation para replicar infraestrutura rapidamente.  
- CloudWatch + CloudTrail = olhos da governança.

**Recursos Úteis**:  
- [CloudWatch Docs](https://docs.aws.amazon.com/cloudwatch/)  
- [CloudTrail Guide](https://docs.aws.amazon.com/cloudtrail/)  
- [CloudFormation Templates](https://docs.aws.amazon.com/cloudformation/)  
- [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
