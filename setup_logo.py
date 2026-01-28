"""
Script para adicionar a logo do ATIVA ao projeto.
Copie o arquivo logo.png para a pasta static manualmente usando:
- Copie a imagem logo.png para: static/logo.png

Ou use este script se tiver a imagem em outro local.
"""

import os
import shutil

# Caminho esperado da logo
static_path = os.path.join(os.path.dirname(__file__), 'static')
logo_path = os.path.join(static_path, 'logo_distribuidora.png')

# Criar pasta static se não existir
os.makedirs(static_path, exist_ok=True)

if os.path.exists(logo_path):
    print("Logo ja existe em: " + logo_path)
else:
    print("Logo nao encontrada em: " + logo_path)
    print("\nPor favor, copie o arquivo logo_distribuidora.png para: static/logo_distribuidora.png")
    print("Depois disso, o logo aparecera automaticamente no site e nos PDFs.")
