# 📊 Dashboard de Análise de Registros

## Descrição

O novo **Dashboard de Análise** foi criado para fornecer uma visualização interativa dos dados de pedidos registrados no sistema. Com gráficos dinâmicos e responsivos, é possível acompanhar as principais métricas do seu negócio em tempo real.

## 🎯 Funcionalidades

### Estatísticas Principais
O dashboard apresenta 3 cards com as principais métricas:
- **💰 Total de Vendas**: Soma de todos os valores dos pedidos
- **📦 Total de Pedidos**: Quantidade total de pedidos registrados
- **📊 Ticket Médio**: Valor médio por pedido

### Gráficos Interativos

#### 🛍️ Produtos Mais Vendidos
Gráfico de barras horizontal mostrando os 10 produtos com maior quantidade vendida.
- **Interatividade**: Passe o mouse para ver detalhes
- **Cor**: Verde (tema principal)

#### 👥 Clientes Top
Gráfico de pizza mostrando a distribuição dos seus top 10 clientes por número de pedidos.
- **Interatividade**: Clique para destacar/ocultar clientes
- **Cores**: Variadas para melhor visualização

#### 📈 Vendas por Data
Gráfico de linha com área preenchida mostrando a evolução das vendas ao longo do tempo.
- **Interatividade**: Hover para ver valores exatos
- **Recurso**: Zoom e pan disponíveis

#### 💳 Valores por Cliente
Gráfico de barras vertical mostrando o valor total gasto pelos top 10 clientes.
- **Interatividade**: Hover para ver valores em reais
- **Cor**: Amarelo/Ouro (tema secundário)

## 🎨 Design

O dashboard foi desenvolvido com:
- **Tema Escuro**: Combinando com o design do site
- **Cores Principais**: Verde (#10b981) e Amarelo (#fbbf24)
- **Responsive**: Funciona em dispositivos móveis, tablets e desktops
- **Plotly**: Biblioteca moderna para gráficos interativos

## 🚀 Como Usar

### Acessar o Dashboard
1. Acesse a página de Registros: `http://localhost:5001/registros`
2. Clique no botão **"📊 Dashboards"** no menu superior
3. Ou acesse direto: `http://localhost:5001/dashboards`

### Menu de Abas
- **📋 Registros**: Volta para a lista de pedidos
- **📊 Dashboards**: Página atual com os gráficos
- **🚪 Sair**: Faz logout do sistema

### Interação com Gráficos
- **Hover**: Passe o mouse para ver valores detalhados
- **Clique**: Em gráficos de pizza, clique para destacar categorias
- **Zoom**: Use o botão de zoom (canto superior direito de cada gráfico)
- **Reset**: Clique em "Reset axes" para voltar à visualização original
- **Download**: Clique no ícone de câmera para baixar o gráfico como imagem

## 📊 Dados Analisados

Os gráficos utilizam informações dos pedidos registrados:
- **Cliente**: Nome do cliente
- **Data**: Data do pedido
- **Produtos**: Itens vendidos com quantidade
- **Valores**: Preço e valor total de cada venda

## ⚙️ Dados Vazios

Quando não há pedidos registrados, o dashboard exibe uma mensagem indicando que não há dados disponíveis. Os gráficos aparecerão automaticamente assim que os primeiros pedidos forem registrados no sistema.

## 📱 Responsividade

O dashboard se adapta automaticamente para:
- **Desktop**: Gráficos lado a lado em 2 colunas
- **Tablet**: Gráficos em 1 coluna
- **Mobile**: Todos os elementos em coluna única com toque responsivo

## 🔒 Segurança

O acesso ao dashboard é restrito e requer:
- **Autenticação**: Login com senha do sistema
- **Sessão**: Mantida durante a navegação
- **Logout**: Sair limpa completamente a sessão

---

**Versão**: 1.0  
**Data**: Janeiro 2026  
**Desenvolvido com**: Flask + Plotly + Python
