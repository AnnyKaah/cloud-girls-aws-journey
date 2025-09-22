# Módulo 5 – Práticas e Exercícios

## 🚀 Hands-on realizados

1. **Criando banco de dados RDS**
   - Serviço: Amazon RDS → Launch DB Instance  
   - Engine: MySQL (ou PostgreSQL)  
   - Configurações: Multi-AZ, Storage 20GB, Backups habilitados  
   - Conectar via cliente MySQL Workbench ou terminal

2. **Explorando DynamoDB**
   - Criar tabela: `Usuarios`  
   - Chave primária: `user_id`  
   - Inserir itens de teste (ex.: nome, email, data_cadastro)  
   - Habilitar backups on-demand

3. **Backup e Recuperação**
   - RDS: criar snapshot manual  
   - RDS: restaurar snapshot em nova instância  
   - DynamoDB: criar backup on-demand e restaurar tabela  
   - S3: ativar versionamento em bucket de teste  

## 📝 Observações

- RDS é ótimo para aplicações com **relacionamentos complexos** e transações  
- DynamoDB é ideal para **alto volume e latência baixa**  
- Testar recuperação é tão importante quanto criar backup  

## 📂 Imagens e Diagramas

- [Exemplo RDS Dashboard](diagramas/rds-dashboard.png)  
- [Exemplo DynamoDB Table](diagramas/dynamodb-table.png)  
- [Exemplo fluxo Backup/Restore](diagramas/backup-restore.png)
