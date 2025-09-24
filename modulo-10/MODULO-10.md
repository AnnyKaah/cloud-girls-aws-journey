# Módulo 10: Desenvolvimento e Ferramentas na AWS

**Resumo Geral**:  
Explora ferramentas para desenvolvimento de aplicações AWS, incluindo SDKs, CLI, SAM (Serverless Application Model) e integração com ambientes de desenvolvimento locais (VS Code, LocalStack). Constrói sobre Lambda/EC2 (Módulos 2-3), IAM (Módulo 8) e prepara para DevOps (Módulo 11).  


---

## Seção 1: Ferramentas de Desenvolvimento AWS (SDKs e CLI Avançados)

- **Introdução**: SDKs e CLI permitem construir apps nativos AWS; integre com linguagens como Python, Node.js ou Java.
- **AWS SDKs**: Use Boto3 (Python) ou AWS SDK for JavaScript para interagir com serviços.
- **AWS CLI**: Comandos avançados, scripting e integração com pipelines (`--output json | jq`).
- **Instalação**: Configure perfis IAM múltiplos (`aws configure --profile dev`) e instale SDKs via pip/npm.

**Diagrama Mermaid – Fluxo SDK/CLI**: [sdk-cli.mmd](diagrams/sdk-cli.mmd)

**Exemplo de código (Boto3 SDK)**: [boto3_create_table.py](exemplos/boto3_create_table.py)

---

## Seção 2: AWS SAM para Desenvolvimento Serverless

- **O que é SAM**: Framework para build, test e deploy de apps serverless (Lambda + API Gateway + DynamoDB).
- **Desenvolvendo com SAM**: Crie templates `sam.yaml` e use `sam build/deploy`.
- **Testes Locais**: `sam local invoke` para simular Lambdas sem deploy.
- **Integração com IDEs**: AWS Toolkit para VS Code, debug via Docker.

**Diagrama Mermaid – Fluxo Serverless SAM**: [sam-flow.mmd](diagrams/sam-flow.mmd)

---

## Seção 3: Ambientes de Desenvolvimento Local e Integração

- **LocalStack**: Simule serviços AWS localmente via Docker (`docker run -p 4566:4566 localstack/localstack`).
- **Integração IDEs/Ferramentas**: VS Code + AWS Toolkit, Postman para APIs.
- **Debugging & Versionamento**: X-Ray, Git.
- **Melhores Práticas**: Perfis IAM restritos, teste local antes de produção.

**Diagrama Mermaid – Desenvolvimento Local com LocalStack**: [localstack.mmd](diagrams/localstack.mmd)

---

## Seção 4: Desafio de Projeto

**Implementando Infraestrutura Automatizada com AWS CloudFormation**

- Templates CloudFormation para Lambda, API Gateway e DynamoDB.
- Deploy via SAM CLI / CLI AWS.
- Automação de roles IAM para Lambdas (least privilege).
- Redução de setup de horas para minutos.

**Referência**: [Desafio de Projeto Módulo 10](desafios/modulo10)

---

## Recursos Úteis

- [AWS SDK Documentation](https://aws.amazon.com/developer/)
- [AWS CLI Reference](https://docs.aws.amazon.com/cli/)
- [AWS SAM Developer Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)
- [LocalStack Docs](https://docs.localstack.cloud/)
