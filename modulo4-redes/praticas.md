# Módulo 4 – Práticas e Exercícios

## 🚀 Hands-on realizados

1. **Criar VPC personalizada**
   - CIDR: `10.0.0.0/16`  
   - Criar 2 subnets: pública (`10.0.1.0/24`) e privada (`10.0.2.0/24`)  
   - Criar Internet Gateway para subnets públicas  

2. **Configurar Security Groups**
   - Grupo EC2-Web:
     - Entrada: Porta 22 (SSH) → seu IP
     - Entrada: Porta 80 (HTTP) → qualquer lugar
     - Saída: Tudo permitido
   - Aplicar grupo a uma instância EC2

3. **Configurar Route 53**
   - Criar domínio de teste  
   - Apontar para IP público da instância EC2  

4. **Distribuição com CloudFront**
   - Criar distribuição para conteúdo do bucket S3  
   - Observar URL gerada para acesso global  

5. **Elastic Load Balancer**
   - Criar ALB  
   - Adicionar 2 instâncias EC2 como targets  
   - Configurar health check e listener na porta 80  

## 📝 Observações

- Sempre alinhar regiões de EC2, S3 e CloudFront para reduzir latência e custo  
- Security Groups isolam serviços e previnem ataques externos  
- ALB permite escalar horizontalmente aplicações sem interrupção  

## 📂 Imagens e Diagramas

- [Exemplo VPC + Subnets](diagramas/vpc-subnets.png)  
- [Exemplo ELB + EC2](diagramas/ELB%20+%20EC2.gif)  
- [Exemplo CloudFront + S3](diagramas/cloudfront-s3.jpeg)
