# Módulo 2 – Práticas e Exercícios

## 🚀 Hands-on realizados

1. **Criar Instância EC2**
   - Abrir AWS Management Console → EC2 → Launch Instance  
   - Escolher AMI (Linux ou Windows)  
   - Selecionar tipo de instância (ex.: t2.micro para teste)  
   - Configurar Security Group: liberar SSH (Linux) ou RDP (Windows)  
   - Lançar a instância

2. **Configurar EBS**
   - Volume padrão já anexado à instância  
   - Criar volumes adicionais se necessário (ex.: 10GB SSD)  
   - Anexar volume à instância e montar (Linux: `mount /dev/xvdf /mnt/data`)  

3. **Criar Bucket no S3**
   - Navegar para S3 → Create bucket  
   - Nome único global, escolher região  
   - Configurar permissões (pública ou privada)  
   - Upload de arquivos de teste (ex.: imagens ou logs)  

4. **Desafio Draw.io**
   - Criar diagrama representando:  
     ```
     Usuário → EC2 → EBS
            ↘ Lambda → S3
     ```
   - Salvar diagrama na pasta `diagramas/`  

## 📝 Observações

- Sempre selecionar a **mesma região** para EC2, EBS e S3 para evitar custos de transferência  
- Security Group é fundamental: abrir somente portas necessárias  
- Diagrama ajuda a visualizar fluxo de dados e arquitetura real  

## 📂 Imagens e Diagramas

- [Exemplo EC2 Dashboard](diagramas/ec2-dashboard.png)  
- [Exemplo arquitetura EC2 + S3 + Lambda](diagramas/arquitetura-ec2-s3-lambda.png)
