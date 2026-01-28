from flask import Flask, render_template, session, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
from collections import Counter
import json

# Definir o caminho do banco de dados na pasta raiz do projeto (compartilhado)
basedir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(basedir)
db_path = os.path.join(parent_dir, 'pedidos.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui_2024'
db = SQLAlchemy(app)

# ---------- MODELO DE BANCO DE DADOS ----------
class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(100), nullable=False)
    data = db.Column(db.String(10), nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.now)
    itens = db.Column(db.JSON, nullable=False)  # JSON com os itens do pedido
    valor_total = db.Column(db.Float, default=0)
    
    def __repr__(self):
        return f'<Pedido {self.id} - {self.cliente}>'

# Criar tabelas
with app.app_context():
    db.create_all()

# ---------- AUTENTICAÇÃO ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    from flask import request
    if request.method == "POST":
        senha = request.form.get("senha")
        # Senha padrão: "@Sapatolandia1"
        if senha == "@Sapatolandia1":
            session['logado'] = True
            return redirect("/registros")
        else:
            return render_template("login.html", erro="Senha incorreta!")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

# ---------- ROTAS ----------
@app.route("/")
def index():
    if not session.get('logado'):
        return redirect("/login")
    return redirect("/registros")

# REGISTROS DO SISTEMA (ACESSO RESTRITO)
@app.route("/registros")
def registros():
    if not session.get('logado'):
        return redirect("/login")
    
    # Buscar todos os pedidos do banco de dados
    pedidos = Pedido.query.order_by(Pedido.data_criacao.desc()).all()
    
    # Calcular total geral
    total_geral = sum(p.valor_total for p in pedidos)
    
    return render_template("registros.html", pedidos=pedidos, total_geral=total_geral)

# DELETAR PEDIDO
@app.route("/deletar_pedido/<int:pedido_id>")
def deletar_pedido(pedido_id):
    if not session.get('logado'):
        return redirect("/login")
    
    pedido = Pedido.query.get(pedido_id)
    if pedido:
        db.session.delete(pedido)
        db.session.commit()
    
    return redirect("/registros")

# DASHBOARDS
@app.route("/dashboards")
def dashboards():
    if not session.get('logado'):
        return redirect("/login")
    
    # Buscar todos os pedidos
    pedidos = Pedido.query.all()
    
    # Preparar dados para os gráficos
    dados_graficos = preparar_dados_graficos(pedidos)
    
    return render_template("dashboards.html", dados_graficos=json.dumps(dados_graficos))

def preparar_dados_graficos(pedidos):
    """Prepara os dados para os gráficos do dashboard"""
    
    # Contadores e totalizadores
    clientes = []
    produtos = Counter()
    datas = []
    valores = []
    valores_por_data = {}
    valores_por_cliente = {}
    
    for pedido in pedidos:
        # Clientes
        clientes.append(pedido.cliente)
        
        # Datas e Valores
        data = pedido.data
        valor = pedido.valor_total
        datas.append(data)
        valores.append(valor)
        
        # Valores por data
        if data not in valores_por_data:
            valores_por_data[data] = 0
        valores_por_data[data] += valor
        
        # Valores por cliente
        if pedido.cliente not in valores_por_cliente:
            valores_por_cliente[pedido.cliente] = 0
        valores_por_cliente[pedido.cliente] += valor
        
        # Produtos
        for item in pedido.itens:
            quantidade = float(item['quantidade']) if isinstance(item['quantidade'], str) else item['quantidade']
            produtos[item['produto']] += quantidade
    
    # Contar clientes
    clientes_counter = Counter(clientes)
    
    return {
        'clientes_top': dict(clientes_counter.most_common(10)),
        'produtos_vendidos': dict(produtos.most_common(10)),
        'valores_por_data': dict(sorted(valores_por_data.items())),
        'valores_por_cliente': dict(sorted(valores_por_cliente.items(), key=lambda x: x[1], reverse=True)[:10]),
        'total_pedidos': len(pedidos),
        'total_vendas': sum(p.valor_total for p in pedidos),
        'valor_medio': sum(p.valor_total for p in pedidos) / len(pedidos) if pedidos else 0,
        'produtos_top': dict(produtos.most_common(5)),
        'datas_chronologicas': sorted(set(datas)),
    }

if __name__ == "__main__":
    app.run(debug=True, port=5001)
