import json
import os

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

def mostrar_status():
    bloqueio = carregar_bloqueio()
    status = "🔴 BLOQUEADO" if bloqueio["bloqueado"] else "🟢 DESBLOQUEADO"
    print(f"\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"  Status do Sistema: {status}")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

print("\n╔════════════════════════════════════════╗")
print("║   ATIVA - Gerenciador do Sistema      ║")
print("╚════════════════════════════════════════╝\n")
print("Comandos disponíveis:")
print("  /bloquear      - Bloquear acesso ao sistema")
print("  /desbloquear   - Desbloquear acesso ao sistema")
print("  /status        - Ver status atual")
print("  /sair          - Sair do gerenciador\n")

mostrar_status()

while True:
    comando = input("Digite um comando: ").strip().lower()
    
    if comando == "/bloquear":
        salvar_bloqueio(True)
        print("\n✅ Sistema BLOQUEADO com sucesso!")
        mostrar_status()
    
    elif comando == "/desbloquear":
        salvar_bloqueio(False)
        print("\n✅ Sistema DESBLOQUEADO com sucesso!")
        mostrar_status()
    
    elif comando == "/status":
        mostrar_status()
    
    elif comando == "/sair":
        print("\n👋 Encerrando gerenciador...\n")
        break
    
    else:
        print("\n❌ Comando não reconhecido. Tente /bloquear, /desbloquear, /status ou /sair\n")
