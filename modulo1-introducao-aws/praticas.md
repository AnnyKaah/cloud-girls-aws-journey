# Módulo 1 – Práticas e Exercícios

## 🚀 Hands-on realizados

1. **Criação da conta AWS**  
   - Acesse [AWS](https://aws.amazon.com/)  
   - Crie a conta pessoal com e-mail e informações de pagamento  
   - Ative notificações por e-mail e verifique identidade

2. **Configuração de segurança**  
   - Crie usuário IAM: `dev-bootcamp`  
   - Conceda permissões: `AmazonS3FullAccess` + `AmazonEC2FullAccess`  
   - Ative MFA no usuário

3. **Explorando a AWS Management Console**  
   - Navegue pelos serviços S3, EC2 e Lambda  
   - Observe a localização da região no canto superior direito  
   - Abra CloudWatch e veja métricas básicas (mesmo sem criar recursos)

## 📝 Observações

- É **perigoso usar root** para tarefas do dia a dia → sempre usar IAM  
- Ativar MFA adiciona camada de segurança essencial  
- Escolher a região correta evita custos de transferência de dados e latência alta

## 📂 Imagens e Diagramas

- [Exemplo: Interface do Console AWS](imagens/console-aws.png)  
- [Exemplo: Estrutura Regiões e AZs](imagens/regions-az.png)
