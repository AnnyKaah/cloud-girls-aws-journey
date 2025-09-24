# Módulo 9: Segurança na AWS

**Resumo Geral**  
Este módulo aprofunda práticas de segurança na nuvem, criptografia de dados e proteção contra ameaças web. Constrói sobre IAM e CloudTrail (Módulo 8), Security Groups/VPC (Módulo 4) e armazenamento S3/RDS (Módulos 5-6).  


---

## Seção 1: Explorando Práticas Recomendadas de Segurança na Nuvem

- **Introdução**: Segurança na AWS é um pilar do Well-Architected Framework; foco em prevenção, detecção e resposta a incidentes.  
- **Papel do Usuário na Segurança**: Desenvolvedores configuram recursos corretamente (ex.: políticas IAM restritivas); AWS gerencia infraestrutura subjacente.  
- **Modelo de Responsabilidade Compartilhada**:  
  - AWS: Segurança *da nuvem* (ex.: proteção física, patching de hipervisores).  
  - Cliente: Segurança *na nuvem* (ex.: criptografia em S3, monitoramento com CloudTrail).  
- **Segurança na AWS na Prática**:  
  - Ativar MFA para root/IAM  
  - Usar AWS Shield para DDoS  
  - Implementar logging contínuo com CloudWatch/CloudTrail  
- **Conclusão**: Adote automação (ex.: scans com AWS Inspector) e revise regularmente com AWS Config.

---

**Diagrama**: [Práticas de Segurança na Nuvem](diagrams/seguranca-cloud.mmd)

---

## Seção 2: Entendendo a Criptografia de Dados na AWS

- **Introdução à Criptografia de Dados**: Protege contra vazamentos; AWS oferece ferramentas para dados em repouso e em trânsito.  
- **Dados em Trânsito ou Repouso**:  
  - Trânsito: TLS 1.2+ via HTTPS, VPNs privadas  
  - Repouso: KMS, SSE-S3, TDE em RDS  
- **Na Prática**:  
  - Habilite default encryption em S3 (SSE-KMS)  
  - Crie chaves KMS com rotação automática  
  - CLI:  
    ```bash
    aws s3api put-bucket-encryption --bucket meu-bucket \
    --server-side-encryption-configuration 'file://config.json'
    ```
- **Fluxo de Transação**: Dados criptografados entre usuário → app (Lambda) → storage (S3), com KMS gerenciando chaves e auditoria.

**Diagrama**: [Fluxo de Criptografia](diagrams/criptografia.mmd)

---

## Seção 3: Protegendo Aplicações Web com AWS WAF

- **AWS WAF**: Firewall de Aplicações Web que filtra tráfego HTTP/S para CloudFront, ALB ou API Gateway, bloqueando ataques como SQL injection, XSS e bots.  
- **Na Prática**:  
  - Crie Web ACLs com regras managed (ex.: AWSManagedRulesCommonRuleSet)  
  - Adicione custom rules (ex.: rate limiting a 100 requests/min)  
  - Associe a distribuições CloudFront para proteção global  
  - Monitore bloqueios via CloudWatch

**Diagrama**: [Fluxo de Proteção com WAF](diagrams/waf.mmd)

---

## **Integração com Módulos Anteriores e Benefícios**

| Conceito                  | Função                                 | Integração | Benefício |
|----------------------------|---------------------------------------|------------|-----------|
| MFA & IAM Policies         | Autenticação e least privilege         | Módulo 8   | Reduz acessos indevidos em 95% |
| Criptografia KMS/SSE       | Protege dados em trânsito/repouso      | Módulos 5-6 | Compliance LGPD/GDPR |
| WAF Rules                  | Filtro de tráfego web                  | Módulo 4/6 | Bloqueia 99% de ataques comuns |

---

## Recursos Úteis

- [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)  
- [KMS Documentation](https://docs.aws.amazon.com/kms/)  
- [WAF Developer Guide](https://docs.aws.amazon.com/waf/)  
- [AWS Security Best Practices](https://docs.aws.amazon.com/whitepapers/latest/aws-security-best-practices/)

**Atualizado em**: 24/09/2025  
Bootcamp Progresso: 95%
