# Módulo 1 – Introdução ao Bootcamp Code Girls – AWS Cloud Foundations

## 📌 Resumo
Este módulo apresenta os conceitos básicos da AWS, sua história, infraestrutura global e modelo de negócio. Também aborda conceitos fundamentais como regiões, zonas de disponibilidade e serviços gerenciados, além da criação de conta e práticas de segurança.

---

## 🌍 Visão Geral da AWS

- **Introdução**: A AWS (Amazon Web Services) é uma plataforma de computação em nuvem que fornece serviços escaláveis sob demanda, como armazenamento, computação e bancos de dados.  
- **História**: Lançada em 2006 pela Amazon, a AWS nasceu para atender a demanda de infraestrutura de forma escalável e econômica.  
- **Infraestrutura Global**: A AWS possui datacenters distribuídos globalmente organizados em regiões e zonas de disponibilidade (AZs).  
- **Modelo de Negócio**: Baseado em pay-as-you-go (pague pelo que usar), permitindo startups e grandes empresas escalarem recursos sem investimento inicial em hardware.

---

## ⚙️ Conceitos Fundamentais

- **Regiões** → Localizações físicas de datacenters (ex.: us-east-1, sa-east-1). Escolher a região certa ajuda na latência e conformidade regulatória.  
- **Zonas de Disponibilidade (AZs)** → Conjunto de datacenters isolados dentro de uma região para garantir alta disponibilidade. Ex.: uma região pode ter 3 AZs.  
- **Serviços Gerenciados** → Serviços em que a AWS cuida da infraestrutura, manutenção e atualizações. Ex.: RDS, DynamoDB, S3.

---

## 🔐 Configuração de Conta e Práticas de Segurança

- **Criação de Conta** → Criar conta AWS, configurar informações de pagamento e verificar identidade.  
- **Práticas de Segurança**:  
  - Ativar **MFA (Multi-Factor Authentication)**  
  - Criar **usuários IAM** ao invés de usar a conta root  
  - Definir **políticas de permissões mínimas**  
- **Exemplo prático**: Criar usuário IAM chamado `dev-bootcamp`, com acesso somente a S3 e EC2, e ativar MFA.
