bibliotecas = {}
lixeira = []
def main ():
    while(True):

        print("\n===== MENU =====")
        print("1 - Adicionar biblioteca")
        print("2 - Adicionar pasta")
        print("3 - Adicionar fotos em uma pasta")
        print("4 - Ver bibliotecas")
        print("5 - Transferir para lixeira")
        print("6 - Ver lixeira")
        print("7 - Recuperar da Lixeira") 
        print("0 - Sair")

        menu = input("Escolha uma opção: ").strip()

        match menu:
            case "1":
                # ADICIONAR BIBLIOTECA
                criar_bibliotecas(bibliotecas)
            case "2":
                # ADICIONAR PASTA
                criar_pasta(bibliotecas)
            case "3":
                adicionar_fotos(bibliotecas)
            case "4":
                ver_bibliotecas(bibliotecas)
            case "5":
                transferir(bibliotecas,lixeira)
            case "6":
                ver_lixeira(lixeira)
            case "7":
                recuperar_lixeira(bibliotecas,lixeira)
            case "0":
                # ==========================
                # SAIR
                # ==========================
                print("Encerrando o sistema...")
                break

            case _:
                print("Opção inválida.")

def criar_bibliotecas(bibliotecas):

    while True:
        name_bibliotecas = input("Nome da biblioteca: ").strip()
        if (name_bibliotecas.strip() == ""):
            print("Nome inválido.")
        else:
            break

    if (name_bibliotecas in bibliotecas):
        print("Biblioteca já existe!")
        return False
    else:
        bibliotecas[name_bibliotecas] = {}
        print("Biblioteca criada com sucesso!")
        return True

def criar_pasta(bibliotecas):
    while True:
        name_bibliotecas = input("Nome da biblioteca: ").strip()
        if (name_bibliotecas.strip() == ""):
            print("Nome inválido.")
        else:
            break

    if (name_bibliotecas not in bibliotecas):
        print("Biblioteca não encontrada")
        return False
    else:
        while True:
            nome_pasta = input("Nome da pasta: ").strip()
            if (nome_pasta.strip() == ""):
                print("Nome inválido.")
            else:
                break
        if (nome_pasta in bibliotecas[name_bibliotecas]):
            print("Pasta já existe!")
            return False
        else:
            bibliotecas[name_bibliotecas][nome_pasta] = []
            print("Pasta criada com sucesso!")
            return True

def adicionar_fotos(bibliotecas):
    while (True):
        name_bibliotecas = input("Digite a biblioteca: ").strip()

        if name_bibliotecas.strip() == "":
            print("Nome inválido.")
        else:
            break
    if (name_bibliotecas not in bibliotecas):
        print("Biblioteca não encontrada.")
        return False
    else:
        while (True):
            nome_pasta = input("Digite o nome da Pasta: ").strip()

            if nome_pasta.strip() == "":
                print("Nome inválido.")
            else:
                break;

        if (nome_pasta not in bibliotecas[name_bibliotecas]):
            print("Pasta não encontrada.")
            return False
        else:
            while (True):
                foto = input("Digite o nome da foto: ").strip()

                if foto.strip() == "":
                    print("Nome inválido.")
                else:
                    break;
            if foto in bibliotecas[name_bibliotecas][nome_pasta]:
                print("Essa foto já existe nessa pasta.")
                return False
            else:
                bibliotecas[name_bibliotecas][nome_pasta].append(foto)
                print("Foto Adicionada com sucesso!")
                return True

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

def transferir(bibliotecas,lixeira):
    # ==========================
    # TRANSFERIR LIXEIRA
    # ==========================
    while True:
        print("1 - Transferir biblioteca para lixeira")
        print("2 - Transferir pasta para lixeira")
        print("3 - Transferir foto para lixeira")
        print("0 - Sair")

        op_transf = input("Escolha uma opção: ")

        match op_transf:
            case "1":
                transferir_bibliotecas(bibliotecas,lixeira)
                return
            case "2":
                transferir_pasta(bibliotecas,lixeira)
                return
            case "3":
                transferir_fotos(bibliotecas,lixeira)
                return
            case "0":
                # ==========================
                # SAIR
                # ==========================
                print("Fechando lixeira.")
                return

            case _:
                print("Opção inválida.")

def transferir_bibliotecas(bibliotecas,lixeira):
    while True:
        name_bibliotecas = input("Digite o nome da biblioteca: ")
        if name_bibliotecas.strip() == "":
            print("Nome inválido.")
        else:
            break
    if name_bibliotecas not in bibliotecas:
        print("Biblioteca não encontrada.")
        return False
    else:
        resposta = "x"
        while (True):
            resposta = input("Certeza que deseja deletar? Sim ou não: ").strip().lower()
            if resposta in ["sim", "s", "não", "nao", "n"]:
                break
            else:
                print("Opção inválida. Digite sim ou não.")
        if resposta in ["não", "nao", "n"]:
            print("Operação cancelada.")
            return False
        else:
            nome_final = name_bibliotecas
            contador = 1
            while True:
                ja_existe = False
                for item in lixeira:
                    if item["tipo"] == "biblioteca" and item["biblioteca"] == nome_final:
                        ja_existe = True
                        break

                if ja_existe:
                    nome_final = f"{name_bibliotecas} ({contador})"
                    contador += 1
                else:
                    break
            lixeira.append({
                "tipo": "biblioteca",
                "biblioteca": nome_final,
                "nome_original": name_bibliotecas,
                "conteudo": bibliotecas[name_bibliotecas],
            })
            print("Biblioteca enviada para lixeira.")
            del bibliotecas[name_bibliotecas]
            return True

def transferir_pasta(bibliotecas,lixeira):
    while True:
        name_bibliotecas = input("Digite o nome da biblioteca: ")
        if name_bibliotecas.strip() == "":
            print("Nome inválido.")
        else:
            break

    if name_bibliotecas not in bibliotecas:
        print("Biblioteca não encontrada.")
        return False

    else:
        while True:
            nome_pasta = input("Digite o nome da Pasta: ")

            if nome_pasta.strip() == "":
                print("Nome inválido.")
            else:
                break;

        if nome_pasta not in bibliotecas[name_bibliotecas]:
            print("Pasta não encontrada.")
            return False
        resposta = "x"
        while (True):
            resposta = input("Certeza que deseja deletar? Sim ou não: ")
            if resposta.lower() in ["sim", "s", "não", "nao", "n"]:
                break
            else:
                print("Opção inválida. Digite sim ou não.")
        if resposta.lower() in ["não", "nao", "n"]:
            print("Operação cancelada.")
            return False
        else:
            contador = 1
            nome_final = nome_pasta
            while True:
                ja_existe = False
                for item in lixeira:
                    if (item["tipo"] == "pasta" and item["biblioteca"] == name_bibliotecas and item["nome"] == nome_final):
                        ja_existe = True
                        break

                if ja_existe:
                    nome_final = f"{nome_pasta} ({contador})"
                    contador += 1
                else:
                    break

            lixeira.append({
                "tipo": "pasta",
                "biblioteca": name_bibliotecas,
                "nome": nome_final,
                "conteudo": bibliotecas[name_bibliotecas][nome_pasta]
            })

            del bibliotecas[name_bibliotecas][nome_pasta]

            print("Pasta enviada para lixeira.")
            return True

def transferir_fotos(bibliotecas,lixeira):
    while True:
        name_bibliotecas = input("Digite a biblioteca: ").strip()
        if (name_bibliotecas.strip() == ""):
            print("Nome inválido.")
        else:
            break
    if name_bibliotecas not in bibliotecas:
        print("Biblioteca não encontrada.")
        return False

    else:
        while True:
            nome_pasta = input("Digite a pasta: ")
            if (nome_pasta.strip() == ""):
                print("Nome inválido.")
            else:
                break

        if nome_pasta not in bibliotecas[name_bibliotecas]:
            print("Pasta não encontrada.")
            return False

        else:
            while (True):
                foto = input("Digite o nome da foto: ")

                if foto.strip() == "":
                    print("Nome inválido.")
                else:
                    break;

            if foto not in bibliotecas[name_bibliotecas][nome_pasta]:
                print("Foto não encontrada.")
                return False
            resposta = "x"
            while (True):
                resposta = input("Certeza que deseja deletar? Sim ou não: ")
                if resposta.lower() in ["sim", "s", "não", "nao", "n"]:
                    break
                else:
                    print("Opção inválida. Digite sim ou não.")
            if resposta.lower() in ["não", "nao", "n"]:
                print("Operação cancelada.")
                return False
            else:
                contador = 1
                nome_final = foto
                while True:
                    ja_existe = False
                    for item in lixeira:
                        if item["tipo"] == "foto" and item["biblioteca"] == name_bibliotecas and item["pasta"] == nome_pasta and item["nome"] == nome_final:
                            ja_existe = True
                            break
                    if ja_existe:
                        nome_final = f"{foto} ({contador})"
                        contador += 1
                    else:
                        break

                lixeira.append({
                    "tipo": "foto",
                    "biblioteca": name_bibliotecas,
                    "pasta": nome_pasta,
                    "nome": nome_final
                })

                bibliotecas[name_bibliotecas][nome_pasta].remove(foto)

                print("Foto enviada para lixeira.")
                return True

def ver_lixeira(lixeira):
    if not lixeira:
        print("Lixeira vazia.")
        return False
    else:
        print("\n🗑️ Lixeira:")

        for item in lixeira:
            if (('nome' in item) and item['tipo'] == 'foto'):
                print(f"Foto Apagada: {item['nome']}")
                print(f"Caminho do item: {item['biblioteca']}/{item['pasta']}/{item['nome']}")
            if (('nome' in item) and item['tipo'] == 'pasta'):
                print(f"Pasta Apagada: {item['nome']}")
                print(f"Caminho do item: {item['biblioteca']}/{item['nome']}")
            if (item['tipo'] == 'biblioteca'):
                print(f"Biblioteca Apagada: {item['biblioteca']}")
            print("\n")
        return True

def recuperar_lixeira(bibliotecas,lixeira):
    while True:
        print(" Deseja Recuperar :")
        print("1 - Biblioteca")
        print("2 - Pasta")
        print("3 - Foto")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")
        match opcao:

            case "1":
                recuperar_bibliotecas(bibliotecas, lixeira)
                return
            case "2":
                recuperar_pasta(bibliotecas, lixeira)
                return
            case "3":
                recuperar_foto(bibliotecas, lixeira)
                return
            case "0":
                # ==========================
                # SAIR
                # ==========================
                print("Retornando ao Menu...")
                return
            case _:
                print("Opção inválida.")

def recuperar_bibliotecas(bibliotecas,lixeira):
    print("Biblioteca:")
    while True:
        name_bibliotecas = input("Digite o nome da biblioteca: ").strip()
        if name_bibliotecas == "":
            print("Nome inválido.")
        else:
            break
    busca = None
    for item in lixeira:
        if item["tipo"] == "biblioteca" and item["biblioteca"] == name_bibliotecas:
            busca = item
            break
    if busca == None:
        print("Biblioteca não encontrada.")
        return False
    else:
        resposta = "x"
        while (True):
            resposta = input("Certeza que deseja Recuperar? Sim ou não: ")
            if resposta.lower() in ["sim", "s", "não", "nao", "n"]:
                break
            else:
                print("Opção invalida.Digite sim ou não")
        if resposta.lower() in ["não", "nao", "n"]:
            print("Operação cancelada.")
            return False
        else:
            if name_bibliotecas not in bibliotecas:
                bibliotecas[name_bibliotecas] = {}
            conteudo_recuperado = busca["conteudo"]
            for nome_pasta, fotos in conteudo_recuperado.items():
                if nome_pasta not in bibliotecas[name_bibliotecas]:
                    bibliotecas[name_bibliotecas][nome_pasta] = []
                for foto in fotos:
                    if  foto not in bibliotecas[name_bibliotecas][nome_pasta]:
                        bibliotecas[name_bibliotecas][nome_pasta].append(foto)
            lixeira.remove(busca)
            print("Biblioteca recuperada com sucesso.")

            return True

def recuperar_pasta(bibliotecas,lixeira):
    print("Pasta:")
    while True:
        name_bibliotecas = input("Digite o nome da Biblioteca: ")

        if name_bibliotecas.strip() == "":
            print("Nome inválido.")
        else:
            break;
    while True:
        nome_pasta = input("Digite o nome da Pasta: ")

        if nome_pasta.strip() == "":
            print("Nome inválido.")
        else:
            break;

    busca = None
    for item in lixeira:
        if item["tipo"] == "pasta" and item["biblioteca"] == name_bibliotecas and item[
            "nome"] == nome_pasta:
            busca = item
            break
    if busca == None:
        print("Arquivo não encontrado.")
        return False
    else:
        resposta = "x"
        while (True):
            resposta = input("Certeza que deseja Recuperar? Sim ou não: ")
            if resposta.lower() in ["sim", "s", "não", "nao", "n"]:
                break
            else:
                print("Opção inválida. Digite sim ou não.")
        if resposta.lower() in ["não", "nao", "n"]:
            print("Operação cancelada.")
            return False
        else:
            if name_bibliotecas not in bibliotecas:
                bibliotecas[name_bibliotecas] = {}
            if nome_pasta not in bibliotecas[name_bibliotecas]:
                bibliotecas[name_bibliotecas][nome_pasta] = []
            conteudo_recuperado = busca["conteudo"]
            for foto in conteudo_recuperado:
                if foto not in bibliotecas[name_bibliotecas][nome_pasta]:
                    bibliotecas[name_bibliotecas][nome_pasta].append(foto)

            lixeira.remove(busca)
            print("Pasta recuperada com sucesso.")
            return True

def recuperar_foto(bibliotecas,lixeira):
    print("Foto:")
    while (True):
        name_bibliotecas = input("Digite o nome da Biblioteca: ")

        if name_bibliotecas.strip() == "":
            print("Nome inválido.")
        else:
            break;

    while (True):
        nome_pasta = input("Digite o nome da pasta: ")

        if nome_pasta.strip() == "":
            print("Nome inválido.")
        else:
            break;

    while (True):
        foto = input("Digite o nome da foto: ")

        if foto.strip() == "":
            print("Nome inválido.")
        else:
            break;

    busca = None
    for item in lixeira:
        if item["tipo"] == "foto" and item["biblioteca"] == name_bibliotecas and item[
            "pasta"] == nome_pasta and item["nome"] == foto:
            busca = item
            break
    if busca == None:
        print("Arquivo não encontrado.")
        return False
    else:
        resposta = "x"
        while (True):
            resposta = input("Certeza que deseja Recuperar? Sim ou não: ")
            if resposta.lower() in ["sim", "s", "não", "nao", "n"]:
                break
            else:
                print("Opção inválida. Digite sim ou não.")
        if resposta.lower() in ["não", "nao", "n"]:
            print("Operação cancelada.")
            return False
        else:
            if name_bibliotecas not in bibliotecas:
                bibliotecas[name_bibliotecas] = {}

            if nome_pasta not in bibliotecas[name_bibliotecas]:
                bibliotecas[name_bibliotecas][nome_pasta] = []
            if busca["nome"] in bibliotecas[name_bibliotecas][nome_pasta]:
                print("Essa foto já existe nessa pasta. Não foi possível recuperar.")
                return False
            else:
                bibliotecas[name_bibliotecas][nome_pasta].append(busca["nome"])

                lixeira.remove(busca)

                print("Foto recuperada com sucesso.")
                return True
main()