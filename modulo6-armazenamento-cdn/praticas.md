# Módulo 6 – Práticas e Exercícios

## 🚀 Hands-on realizados

1. **Amazon S3 – Prática**
   - Criar bucket: `bootcamp-modulo6-s3`  
   - Upload de arquivos de teste (ex.: imagens, vídeos)  
   - Configurar versionamento e criptografia  
   - Definir lifecycle rule para mover arquivos antigos para Glacier

2. **Amazon Glacier – Prática**
   - Criar vault: `bootcamp-glacier-vault`  
   - Migrar arquivos do bucket S3 para Glacier  
   - Restaurar arquivo de teste para S3  

3. **CloudFront – Prática**
   - Criar distribuição CloudFront apontando para bucket S3  
   - Configurar cache padrão e comportamento de distribuição  
   - Testar URL gerada globalmente

## 📝 Observações

- Lifecycle rules do S3 ajudam a economizar custos ao arquivar para Glacier  
- Restaurar arquivos do Glacier pode levar algumas horas → planejar estratégias  
- CloudFront requer configuração correta de permissões no bucket para funcionar

## 📂 Imagens e Diagramas

- [Diagrama S3 + Glacier](diagramas/s3-glacier.png)  
- [Diagrama CloudFront + S3](diagramas/cloudfront-s3.jpg)  
