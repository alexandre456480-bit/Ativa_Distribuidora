# 🎯 Sistema de Pedidos ATIVA - Dois Sites

## 📋 Estrutura

Agora você tem dois sites separados:

### 1. **Site Principal** (app.py - porta 5000)
- Página inicial com lista de produtos
- Criação de pedidos
- Gerenciamento de produtos e unidades
- Sistema bloqueado/desbloqueado

### 2. **Site de Registros** (Sistema_Registros/app_registros.py - porta 5001)
- Login restrito com senha
- Visualização de todos os pedidos registrados
- Estatísticas (total de pedidos, valor total, ticket médio)
- Detalhes de cada pedido com itens

## 🚀 Como Rodar

### Terminal 1 - Site Principal:
```bash
python app.py
```
Acesse em: **http://localhost:5000**

### Terminal 2 - Site de Registros:
```bash
cd Sistema_Registros
python app_registros.py
```
Acesse em: **http://localhost:5001**

## 🔐 Credenciais

**Senha de Admin para Registros:** `@Sapatolandia1`

## 📊 Banco de Dados

Ambos os sites compartilham o mesmo banco de dados (`pedidos.db`) localizado na raiz do projeto.

## 📝 Notas

- Os pedidos criados no site principal (porta 5000) aparecerão automaticamente no site de registros (porta 5001)
- Cada site tem seus próprios templates e estilos
- A logo deve estar em `/static/logo.png` (compartilhada ou duplicada)
