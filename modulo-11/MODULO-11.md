# Módulo 11: Automação e DevOps na AWS

**Resumo Geral**:  
Este módulo aprofunda automação, DevOps e CI/CD na AWS. Explora AWS CLI, SDKs, CodeDeploy, Terraform e práticas de DevOps aplicadas. Constrói sobre Lambda/EC2 (Módulos 2-3), IAM (Módulo 8), CloudFormation/SAM (Módulo 10).  


---

## Seção 1: Explorando AWS CLI e SDKs

- **Introdução**: CLI e SDKs permitem automatizar a criação e monitoramento de recursos.
- **AWS SDK**: Boto3 (Python) ou AWS SDK JS para automação programática.
- **AWS CLI**: Execução de scripts, integração em pipelines CI/CD.

**Diagrama Mermaid – Fluxo CLI/SDK**: [cli-sdk.mmd](diagrams/cli-sdk.mmd)  
**Exemplo**: [lambda_s3_trigger.py](exemplos/lambda_s3_trigger.py)

---

## Seção 2: Automatizando Implantação com AWS CodeDeploy

- **O que é CodeDeploy**: Serviço de deploy contínuo para EC2, Lambda e on-premises.
- **Benefícios**: Reduz downtime, permite rollback, integra com CodePipeline.
- **Processo**: Criação de apps, deployment groups e deployment configurations.

**Diagrama Mermaid – Fluxo CodeDeploy**: [code-deploy.mmd](diagrams/code-deploy.mmd)

---

## Seção 3: Criando Recursos com Terraform na AWS

- **O que é Terraform**: IaC para criar recursos declarativamente.
- **Estrutura Terraform**: main.tf, variables.tf, outputs.tf.
- **LocalStack para Testes Locais**: Teste infraestrutura sem custos.
- **Criando e Destruindo Recursos**: `terraform apply` / `terraform destroy`.

**Diagrama Mermaid – Terraform e AWS**: [terraform.mmd](diagrams/terraform.mmd)  
**Exemplo**: [terraform_ec2_s3.tf](exemplos/terraform_ec2_s3.tf)

---

## Seção 4: Introdução e Aplicação de DevOps

- **DevOps**: Cultura de colaboração entre Dev e Ops.
- **Princípios**: CI/CD, automação, monitoramento contínuo.
- **Aplicando na AWS**: CodePipeline + CodeBuild + CodeDeploy.

**Diagrama Mermaid – Fluxo DevOps AWS**: [devops-flow.mmd](diagrams/devops-flow.mmd)

---

## Seção 5: Desafio de Projeto

**Executando Tarefas Automatizadas com Lambda Function e S3**

- Criar função Lambda disparada por eventos em S3.
- Configurar políticas IAM para least privilege.
- Testar logs em CloudWatch e monitoramento.
- Automatizar upload e processamento de arquivos.

**Diagrama Mermaid – Lambda + S3 Trigger**: [lambda-s3.mmd](diagrams/lambda-s3.mmd)

**Referência no README**: [Desafio Módulo 11](desafios/modulo11)

---

## Recursos Úteis

- [AWS CLI Documentation](https://docs.aws.amazon.com/cli/)
- [AWS SDK Documentation](https://aws.amazon.com/developer/)
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [AWS CodeDeploy Guide](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html)
- [AWS Lambda + S3](https://docs.aws.amazon.com/lambda/latest/dg/with-s3.html)
