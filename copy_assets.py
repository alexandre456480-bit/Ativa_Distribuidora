import os
import shutil

# Copiar logo.png para o Sistema_Registros/static
src_logo = r'c:\Users\alexa\OneDrive\Documentos\Sistema_Pedidos\static\logo_distribuidora.png'
dst_dir = r'c:\Users\alexa\OneDrive\Documentos\Sistema_Pedidos\Sistema_Registros\static'

# Criar diretório se não existir
os.makedirs(dst_dir, exist_ok=True)

# Copiar arquivo
if os.path.exists(src_logo):
    shutil.copy2(src_logo, dst_dir)
    print("✅ Logo copiada com sucesso!")
else:
    print("❌ Logo não encontrada na pasta principal")
