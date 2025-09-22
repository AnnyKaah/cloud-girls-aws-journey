# Módulo 3 – Práticas e Exercícios

## 🚀 Hands-on realizados

1. **Criando Instância EC2**
   - AMI: Amazon Linux 2  
   - Tipo: t2.micro  
   - Security Group: SSH liberado para IP próprio  
   - Conectar via MobaXterm usando chave PEM  

2. **Criando Bucket S3**
   - Nome: `bootcamp-codegirls-modulo3`  
   - Região: sa-east-1  
   - Configurar versionamento e criptografia  
   - Upload de arquivos de teste (ex.: `.txt`, `.png`)  

3. **Criando Função Lambda**
   - Runtime: Python 3.9  
   - Código Hello World:  
     ```python
     def lambda_handler(event, context):
         return "Hello World"
     ```  
   - Testar função com evento simples  

4. **Exercício de Integração**
   - Configurar Lambda para escrever/ler arquivos do bucket S3  
   - Verificar permissões no IAM para permitir interação S3 → Lambda  

## 📝 Observações

- Sempre criar **políticas IAM mínimas** para Lambda  
- Testes de Lambda devem começar simples (Hello World) antes de conectar a serviços reais  
- Organizar buckets por módulo ajuda no gerenciamento  

## 📂 Imagens e Diagramas

- [Diagrama EC2 + S3 + Lambda](imagens/arquitetura-modulo3.png)  
- [Exemplo Console Lambda](imagens/lambda-console.png)
