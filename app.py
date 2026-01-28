from flask import Flask, render_template, request, redirect, send_file
import json
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import os

app = Flask(__name__)

# ---------- FUNÇÕES ----------
def carregar_json(arquivo):
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def salvar_json(arquivo, dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def carregar_bloqueio():
    try:
        with open("bloqueio.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"bloqueado": False}

def salvar_bloqueio(bloqueado):
    dados = {"bloqueado": bloqueado}
    with open("bloqueio.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# ---------- ROTAS ----------
@app.route("/")
def index():
    produtos = carregar_json("produtos.json")
    bloqueio = carregar_bloqueio()
    return render_template("index.html", produtos=produtos, sistema_bloqueado=bloqueio["bloqueado"])

@app.route("/sistema")
def sistema():
    return render_template("sistema.html")

# BLOQUEIO/DESBLOQUEIO DO SISTEMA
@app.route("/admin/bloquear-sistema")
def bloquear_sistema():
    salvar_bloqueio(True)
    return {"status": "Sistema bloqueado com sucesso"}

@app.route("/admin/desbloquear-sistema")
def desbloquear_sistema():
    salvar_bloqueio(False)
    return {"status": "Sistema desbloqueado com sucesso"}

# PRODUTOS
@app.route("/produtos", methods=["GET", "POST"])
def produtos():
    produtos = carregar_json("produtos.json")

    if request.method == "POST":
        nome = request.form["nome"]
        produtos.append(nome)
        salvar_json("produtos.json", produtos)
        return redirect("/produtos")

    return render_template("produtos.html", produtos=produtos)

@app.route("/remover_produto/<nome>")
def remover_produto(nome):
    produtos = carregar_json("produtos.json")
    if nome in produtos:
        produtos.remove(nome)
        salvar_json("produtos.json", produtos)
    return redirect("/produtos")

@app.route("/remover_unidade/<nome>")
def remover_unidade(nome):
    unidades = carregar_json("unidades.json")
    if nome in unidades:
        unidades.remove(nome)
        salvar_json("unidades.json", unidades)
    return redirect("/unidades")

# UNIDADES
@app.route("/unidades", methods=["GET", "POST"])
def unidades():
    unidades = carregar_json("unidades.json")

    if request.method == "POST":
        nova = request.form["unidade"]
        unidades.append(nova)
        salvar_json("unidades.json", unidades)
        return redirect("/unidades")

    return render_template("unidades.html", unidades=unidades)

# PEDIDO
@app.route("/pedido", methods=["GET", "POST"])
def pedido():
    produtos = carregar_json("produtos.json")
    unidades = carregar_json("unidades.json")

    if request.method == "POST":
        cliente = request.form["cliente"]
        data = request.form["data"]

        itens = []
        
        # Pega TODOS os produtos que foram preenchidos dinamicamente
        # Iterando pelos nomes dos inputs que começam com "qtd_"
        for key in request.form.keys():
            if key.startswith("qtd_"):
                # Extrai o nome do produto do key
                produto = key.replace("qtd_", "")
                qtd = request.form.get(f"qtd_{produto}")
                
                # Só adiciona se houver quantidade preenchida
                if qtd and qtd.strip():
                    unidade = request.form.get(f"unidade_{produto}", "")
                    preco = request.form.get(f"preco_{produto}", "0")
                    valor = request.form.get(f"valor_{produto}", "0")
                    
                    itens.append({
                        "produto": produto,
                        "quantidade": qtd,
                        "unidade": unidade,
                        "preco": preco,
                        "valor": valor
                    })

        if itens:  # Só gera PDF se houver itens
            gerar_pdf(cliente, data, itens)
            return send_file("pedido.pdf", as_attachment=True)
        else:
            return redirect("/pedido")

    return render_template("pedido.html", produtos=produtos, unidades=unidades)

# ---------- GERAR PDF ----------
def gerar_pdf(cliente, data, itens):
    largura = 40 * mm
    altura = 80 * mm
    
    c = canvas.Canvas("pedido.pdf", pagesize=(largura, altura))
    
    margem = 1.5 * mm
    col_width = (largura - margem * 2) / 5
    
    logo_path = "static/logo_pdf.png"
    valor_total_geral = 0
    line_height = 1.0 * mm
    item_index = 0
    primeira_pagina = True
    
    while item_index < len(itens):
        if not primeira_pagina:
            c.showPage()
        
        primeira_pagina = False
        y = altura - margem
        valor_total_pagina = 0
        
        # Adicionar logo no topo
        if os.path.exists(logo_path):
            try:
                c.drawImage(logo_path, margem, y - 10 * mm, width=37 * mm, height=14 * mm, preserveAspectRatio=True)
            except:
                pass

        y = altura - 8 * mm

        c.setLineWidth(0.5)
        c.line(margem, y, largura - margem, y)
        y -= 2.5 * mm

        c.setFont("Helvetica-Bold", 8)
        c.drawCentredString(largura / 2, y, "PEDIDO")
        y -= 2.5 * mm

        c.setFont("Helvetica", 4.5)
        cliente_display = cliente[:18] if len(cliente) <= 18 else cliente[:15] + "..."
        c.drawString(margem, y, f"Cliente : {cliente_display}")
        
        data_formatted = data.split("-")
        if len(data_formatted) == 3:
            data_display = f"{data_formatted[2]}/{data_formatted[1]}/{data_formatted[0]}"
        else:
            data_display = data
        
        c.drawRightString(largura - margem, y, f"Data: {data_display}")
        y -= 1.8 * mm
        
        c.setLineWidth(0.4)
        c.line(margem, y, largura - margem, y)
        y -= 1.5 * mm
        
        c.setFont("Helvetica-Bold", 3.2)
        c.drawString(margem, y, "Produtos.")
        c.drawString(margem + col_width * 1.3, y, "Qtd")
        c.drawString(margem + col_width * 1.9, y, "Und")
        c.drawString(margem + col_width * 2.4, y, "Unitário")
        c.drawString(margem + col_width * 3.2, y, "Valor")
        
        y -= 1.5 * mm
        c.line(margem, y, largura - margem, y)
        y -= 1.3 * mm
        
        c.setFont("Helvetica", 3)
        
        # Adicionar itens
        while item_index < len(itens):
            item = itens[item_index]
            
            # Espaço reservado para rodapé (total, contato, endereço, assinatura)
            espaco_minimo = 18 * mm
            if y < margem + espaco_minimo:
                break
            
            produto = item["produto"]
            c.drawString(margem, y, produto)
            
            qtd_text = str(item["quantidade"])[:3]
            un_text = str(item["unidade"])
            preco_text = str(item["preco"])[:4]
            
            try:
                valor_num = float(item["valor"]) if item["valor"] else 0
                valor_text = f"R$ {valor_num:.2f}".replace(".", ",")
            except:
                valor_text = "R$ 0,00"
            
            c.drawString(margem + col_width * 1.3, y, qtd_text)
            c.drawString(margem + col_width * 1.9, y, un_text)
            c.drawString(margem + col_width * 2.4, y, preco_text)
            c.drawRightString(largura - margem, y, valor_text)
            
            try:
                valor_num = float(item["valor"]) if item["valor"] else 0
                valor_total_pagina += valor_num
                valor_total_geral += valor_num
            except:
                pass
            
            y -= line_height
            item_index += 1
        
        # Linha separadora final
        c.setLineWidth(0.4)
        c.line(margem, y, largura - margem, y)
        y -= 1.3 * mm
        
        # Valor total DA PÁGINA
        c.setFont("Helvetica-Bold", 3.5)
        valor_total_text = f"Total: R$ {valor_total_pagina:.2f}".replace(".", ",")
        c.drawRightString(largura - margem, y, valor_total_text)
        y -= 1.5 * mm
        
        # Informações de contato
        c.setFont("Helvetica-Bold", 2.5)
        c.drawString(margem, y, "Contato:")
        y -= 0.95 * mm
        
        c.setFont("Helvetica", 2.2)
        c.drawString(margem, y, "(62)3522-9433 / (62)98101-0670 / (62)99978-9984")
        y -= 0.95 * mm
        
        # Endereço
        c.setFont("Helvetica-Bold", 2.5)
        c.drawString(margem, y, "Endereço:")
        y -= 0.95 * mm
        
        c.setFont("Helvetica", 2)
        c.drawString(margem, y, "Rod BR-153 Km 5,5-GP. 03 BOX 07 - CEASA")
        y -= 0.8 * mm
        c.drawString(margem, y, "Jd. Guanabara - Goiania - GO")
        y -= 1 * mm
        
        # Assinatura
        c.setFont("Helvetica-Bold", 2.5)
        c.drawString(margem, y, "Assinatura:")
        y -= 0.9 * mm
        c.setLineWidth(0.3)
        c.line(margem + 3 * mm, y, largura - margem, y)

    c.save()

if __name__ == "__main__":
    app.run(debug=True)