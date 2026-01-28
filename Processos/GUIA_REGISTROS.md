# 📊 GUIA DO SISTEMA DE REGISTROS

## ✅ O Que Foi Implementado

Você agora tem um sistema completo de banco de dados e controle de acesso! Aqui está tudo que foi adicionado:

### 1. **Banco de Dados SQLite**
   - Um arquivo `pedidos.db` será criado automaticamente na primeira execução
   - Todos os pedidos são salvos com:
     - ID único
     - Nome do cliente
     - Data do pedido
     - Data de criação (registro automático)
     - Lista de itens do pedido
     - Valor total calculado

### 2. **Página de Login** 🔐
   - Acesse: `http://localhost:5000/login`
   - **Senha padrão: `admin123`**
   - Personalize no arquivo `app.py` (linha 63) alterando `"admin123"` para sua senha

### 3. **Página de Registros** 📊
   - Acesse: `http://localhost:5000/registros` (após fazer login)
   - Apenas você pode acessar (com a senha)
   - Mostra:
     - **Total de Pedidos**: Quantidade total de pedidos cadastrados
     - **Total Geral**: Soma do valor de todos os pedidos
     - **Ticket Médio**: Valor médio por pedido
     - **Tabela de Pedidos**: Com cliente, data, valor e opção para ver os itens
     - **Detalhamento**: Clique em "📋 Ver Itens" para expandir e ver os produtos

### 4. **Fluxo de Cadastro**
   Quando um cliente faz um pedido:
   1. Clica em "🧾 Acessar Sistema de Pedidos"
   2. Preenche nome, data e produtos
   3. Clica em "📄 Gerar PDF e Registrar Pedido"
   4. O pedido é:
      - **Salvo no banco de dados** (você verá em Registros)
      - **PDF gerado** para o cliente

### 5. **Novo Botão na Home** 🎯
   - Homepage agora tem um botão "📊 Acessar Registros" (azul)
   - Leva para a página de login

---

## 🚀 Como Usar

### 1. Inicie o servidor
```bash
python app.py
```

### 2. Acesse a home
```
http://localhost:5000
```

### 3. Cliente fazer pedido
- Clique em "🧾 Acessar Sistema de Pedidos"
- Preencha os dados
- Clique em "Gerar PDF e Registrar"
- O pedido é registrado automaticamente

### 4. Ver os Registros
- Clique em "📊 Acessar Registros" na home
- Digite a senha: `admin123`
- Veja todos os pedidos registrados

---

## 🔒 Segurança

### Mudar a Senha (RECOMENDADO)
1. Abra `app.py`
2. Procure a linha 63 (dentro da função `login()`)
3. Altere `"admin123"` para sua senha

**Antes:**
```python
if senha == "admin123":
```

**Depois:**
```python
if senha == "sua_nova_senha":
```

4. Salve o arquivo
5. Reinicie o servidor

---

## 📁 Arquivos Modificados/Criados

✅ **app.py** - Adicionado:
  - Banco de dados SQLAlchemy
  - Modelo Pedido
  - Rotas de login/logout/registros
  - Salvamento automático de pedidos

✅ **templates/login.html** - Novo arquivo
  - Página de login responsiva

✅ **templates/registros.html** - Novo arquivo
  - Dashboard de pedidos

✅ **templates/index.html** - Modificado
  - Novo botão para acessar registros

✅ **requirements.txt** - Atualizado
  - Adicionado `flask-sqlalchemy` e `werkzeug`

---

## 💡 Dicas e Funcionalidades

### Ver Detalhes dos Itens
- Na tabela de registros, clique em "📋 Ver Itens" para expandir/retrair
- Mostra produto, quantidade, unidade, preço e valor total

### Filtrar por Data
- Você pode adicionar filtros personalizados em `registros.html` se quiser
- Os pedidos estão ordenados por data mais recente primeiro

### Exportar Dados
- Os dados estão em formato JSON dentro do banco SQLite
- Você pode criar relatórios customizados se precisar

### Backup
- O banco de dados `pedidos.db` fica na raiz do projeto
- Faça backup regularmente!

---

## ⚠️ Importante

1. **Senha**: Mude a senha padrão assim que possível
2. **SECRET_KEY**: No ambiente de produção, altere a `SECRET_KEY` em `app.py`
3. **Backup**: Faça backup do arquivo `pedidos.db` regularmente
4. **Cookies de Sessão**: Os usuários permanecem logados enquanto o navegador estiver aberto

---

## 🔧 Troubleshooting

### Erro: "pedidos.db não encontrado"
- Não se preocupe! O arquivo será criado automaticamente na primeira execução

### Erro: "Módulo não encontrado"
- Execute: `pip install -r requirements.txt`

### Tabela não mostra pedidos
- Reinicie o servidor
- Confirme que o pedido foi salvo corretamente (verifique o PDF)

---

## 📞 Próximas Melhorias Possíveis

Se quiser adicionar no futuro:
- ✅ Exportar relatórios em PDF
- ✅ Filtros por data/cliente
- ✅ Gráficos de vendas
- ✅ Sistema de múltiplos usuários
- ✅ Edição de pedidos registrados
- ✅ Exclusão de pedidos

Aproveite! 🎉
