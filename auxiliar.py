def digitar_nome_bibliotecas():
    while True:
        name_bibliotecas = input("Nome da biblioteca: ").strip()
        if (name_bibliotecas.strip() == ""):
            print("Nome inválido.")
        else:
            return name_bibliotecas

def digitar_nome_pasta():
    while True:
        nome_pasta = input("Nome da pasta: ").strip()
        if (nome_pasta.strip() == ""):
            print("Nome inválido.")
        else:
            return nome_pasta

def digitar_nome_fotos():
    while (True):
        foto = input("Digite o nome da foto: ").strip()

        if foto.strip() == "":
            print("Nome inválido.")
        else:
            return foto

def ver_bibliotecas(bibliotecas):
    if not bibliotecas:
        print("Nenhuma biblioteca cadastrada.")
        return False
    else:
        for biblioteca, pasta in bibliotecas.items():
            print(f"\n📚 Bibliotecas: {biblioteca}")
            for pasta, fotos in pasta.items():
                print(f" 📁 Pasta: {pasta}")
                if (fotos):
                    for foto in fotos:
                        print(f"  🖼️ {foto}")
                else:
                    print("  Pasta vazia.")
        return True
def confirmacao():
    while (True):
        resposta = input("Tem Certeza que deseja Fazer isso? Sim ou não: ").strip().lower()
        if resposta in ["sim", "s", "não", "nao", "n"]:
            return resposta
        else:
            print("Opção inválida. Digite sim ou não.")