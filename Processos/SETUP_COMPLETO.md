# ✅ SETUP COMPLETO - SISTEMA DE REGISTROS

## O que foi feito:

### 1️⃣ Criado **Site de Registros Separado**
- Pasta: `Sistema_Registros/`
- App: `app_registros.py` (porta 5001)
- Templates e estilos próprios

### 2️⃣ Modificado **Site Principal**
- Removida a rota `/registros` do `app.py`
- Login agora redireciona para `http://localhost:5001`
- Site principal (porta 5000) mantém apenas funções de pedido

### 3️⃣ Compartilhamento de Dados
- Ambos os sites usam o mesmo banco de dados: `pedidos.db`
- Pedidos criados no site 5000 aparecem em 5001

### 4️⃣ Assets Copiados
- Logo copiada para `Sistema_Registros/static/`
- Estilos CSS duplicados

---

## 🚀 PARA RODAR:

### Terminal 1 - Site de Pedidos (5000)
```bash
python app.py
```
Abra: http://localhost:5000

### Terminal 2 - Site de Registros (5001)
```bash
cd Sistema_Registros
python app_registros.py
```
Abra: http://localhost:5001

### Senha de Admin
```
@Sapatolandia1
```

---

## 📊 RESUMO DA ARQUITETURA

```
                    COMPARTILHADO
                    pedidos.db
                        ↑
                    ↙      ↖
            
Port 5000               Port 5001
(app.py)              (app_registros.py)
├─ Pedidos            ├─ Login
├─ Produtos           ├─ Registros
└─ Unidades           └─ Estatísticas
```

---

## ✨ Próximas Etapas (Opcional)

- [ ] Adicionar autenticação mais segura (hash de senha)
- [ ] Criar páginas de edição/exclusão de pedidos
- [ ] Adicionar exportação de relatórios (PDF/Excel)
- [ ] Implementar filtros avançados nos registros
- [ ] Setup com Docker para facilitar deployment

---

**Status:** ✅ Pronto para usar!
