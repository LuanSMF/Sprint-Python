bibliotecas = {}
lixeira = []
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

    menu = input("Escolha uma opção: ")

    match menu:
        case "1":
            # ==========================
            # ADICIONAR BIBLIOTECA
            # ==========================
            while True:
                name_bibliotecas = input("Nome da biblioteca: ")
                if(name_bibliotecas.strip() == ""):
                    print("Nome inválido.")
                else:
                    break

            if(name_bibliotecas in bibliotecas):
                print("Biblioteca já existe!")
            else:
                bibliotecas[name_bibliotecas] = {}
                print("Biblioteca criada com sucesso!")

        case "2":
            # ==========================
            # ADICIONAR PASTA
            # ==========================
            while True:
                name_bibliotecas = input("Nome da biblioteca: ")
                if (name_bibliotecas.strip() == ""):
                    print("Nome inválido.")
                else:
                    break

            if(name_bibliotecas not in bibliotecas):
                print("Biblioteca não encontrada")
            else:
                while True:
                    nome_pasta = input("Nome da pasta: ")
                    if (nome_pasta.strip() == ""):
                        print("Nome inválido.")
                    else:
                        break
                if(nome_pasta  in bibliotecas[name_bibliotecas]):
                    print("Pasta já existe!")
                else:
                    bibliotecas[name_bibliotecas][nome_pasta] = []
                    print("Pasta criada com sucesso!")
        case "3":
            # ==========================
            # ADICIONAR FOTOS
            # ==========================
            while (True):
                name_bibliotecas = input("Digite a biblioteca: ")

                if name_bibliotecas.strip() == "":
                    print("Nome inválido.")
                else:
                    break
            if(name_bibliotecas not in bibliotecas):
                print("Biblioteca não encontrada.")
            else:
                while (True):
                    nome_pasta = input("Digite o nome da Pasta: ")

                    if nome_pasta.strip() == "":
                        print("Nome inválido.")
                    else:
                        break;

                if(nome_pasta not in bibliotecas[name_bibliotecas]):
                    print("Pasta não encontrada.")
                else:
                    while(True):
                        foto = input("Digite o nome da foto: ")

                        if foto.strip() == "":
                            print("Nome inválido.")
                        else:
                            break;
                    if foto in bibliotecas[name_bibliotecas][nome_pasta]:
                        print("Essa foto já existe nessa pasta.")
                    else:
                        bibliotecas[name_bibliotecas][nome_pasta].append(foto)
                        print("Foto Adicionada com sucesso!")
        case "4":
            # ==========================
            # VER BIBLIOTECAS
            # ==========================
            if not bibliotecas:
                print("Nenhuma biblioteca cadastrada.")
            else:
                for biblioteca,pasta in bibliotecas.items():
                    print(f"\n📚 Bibliotecas: {biblioteca}")
                    for pasta,fotos in pasta.items():
                        print(f" 📁 Pasta: {pasta}")
                        if(fotos):
                            for foto in fotos:
                                print(f"  🖼️ {foto}")
                        else:
                            print("  Pasta vazia.")
        case "5":
            # ==========================
            # TRANSFERIR LIXEIRA
            # ==========================
            while True:
                print("1 - Transferir biblioteca para lixeira")
                print("2 - Transferir pasta para lixeira")
                print("3 - Transferir foto para lixeira")
                print("0 - Sair")

                transf = input("Escolha uma opção: ")

                match transf:
                        case "1":
                            while True:
                                name_bibliotecas = input("Digite o nome da biblioteca: ")
                                if name_bibliotecas.strip() == "":
                                    print("Nome inválido.")
                                else:
                                    break
                            if name_bibliotecas not in bibliotecas:
                                print("Biblioteca não encontrada.")
                            else:
                                resposta="x"
                                while (True):
                                    resposta= input("Certeza que deseja deletar? Sim ou não: ")
                                    if resposta.lower() in ["sim", "s","não", "nao", "n"]:
                                        break
                                    else:
                                        print("Opção inválida. Digite sim ou não.")
                                if resposta.lower() in ["não", "nao", "n"]:
                                    print("Operação cancelada.")
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
                                        "conteudo": bibliotecas[name_bibliotecas]
                                    })
                                    print("Biblioteca enviada para lixeira.")
                                    del bibliotecas[name_bibliotecas]

                        case "2":
                            while True:
                                name_bibliotecas = input("Digite o nome da biblioteca: ")
                                if name_bibliotecas.strip() == "":
                                    print("Nome inválido.")
                                else:
                                    break

                            if name_bibliotecas not in bibliotecas:
                                print("Biblioteca não encontrada.")

                            else:
                                while True:
                                    nome_pasta = input("Digite o nome da Pasta: ")

                                    if nome_pasta.strip() == "":
                                        print("Nome inválido.")
                                    else:
                                        break;

                                if nome_pasta not in bibliotecas[name_bibliotecas]:
                                    print("Pasta não encontrada.")
                                    continue
                                resposta = "x"
                                while (True):
                                    resposta = input("Certeza que deseja deletar? Sim ou não: ")
                                    if resposta.lower() in ["sim", "s", "não", "nao", "n"]:
                                        break
                                    else:
                                        print("Opção inválida. Digite sim ou não.")
                                if resposta.lower() in ["não", "nao", "n"]:
                                    print("Operação cancelada.")
                                else:
                                    contador = 1
                                    nome_final = nome_pasta
                                    while True:
                                        ja_existe = False
                                        for item in lixeira:
                                            if item["tipo"] == "pasta" and item["nome"] == nome_final:
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
                        case "3":
                            while True:
                                name_bibliotecas = input("Digite a biblioteca: ")
                                if (name_bibliotecas.strip() == ""):
                                    print("Nome inválido.")
                                else:
                                    break
                            if name_bibliotecas not in bibliotecas:
                                print("Biblioteca não encontrada.")

                            else:
                                while True:
                                    nome_pasta = input("Digite a pasta: ")
                                    if (nome_pasta.strip() == ""):
                                        print("Nome inválido.")
                                    else:
                                        break

                                if nome_pasta not in bibliotecas[name_bibliotecas]:
                                    print("Pasta não encontrada.")

                                else:
                                    while (True):
                                        foto = input("Digite o nome da foto: ")

                                        if foto.strip() == "":
                                            print("Nome inválido.")
                                        else:
                                            break;

                                    if foto not in bibliotecas[name_bibliotecas][nome_pasta]:
                                        print("Foto não encontrada.")
                                        continue
                                    resposta = "x"
                                    while (True):
                                        resposta = input("Certeza que deseja deletar? Sim ou não: ")
                                        if resposta.lower() in ["sim", "s", "não", "nao", "n"]:
                                            break
                                        else:
                                            print("Opção inválida. Digite sim ou não.")
                                    if resposta.lower() in ["não", "nao", "n"]:
                                        print("Operação cancelada.")
                                    else:
                                        contador = 1
                                        nome_final = foto
                                        while True:
                                            ja_existe = False
                                            for item in lixeira:
                                                if item["tipo"] == "foto" and item["nome"] == nome_final:
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
                        case "0":
                        # ==========================
                        # SAIR
                        # ==========================
                            print("Fechando lixeira.")
                            break

                        case _:
                            print("Opção inválida.")

        case "6":
                # ==========================
                # VER LIXEIRA
                # ==========================

                if not lixeira:
                    print("Lixeira vazia.")

                else:
                    print("\n🗑️ Lixeira:")

                    for item in lixeira:
                        if(('nome' in item) and item['tipo'] == 'foto'):
                            print(f"Foto Apagada: {item['nome']}")
                            print(f"Caminho do item: {item['biblioteca']}/{item['pasta']}/{item['nome']}")
                        if(('nome' in item) and item['tipo'] == 'pasta'):
                            print(f"Pasta Apagada: {item['nome']}")
                            print(f"Caminho do item: {item['biblioteca']}/{item['nome']}")
                        if(item['tipo'] == 'biblioteca'):
                            print(f"Biblioteca Apagada: {item['biblioteca']}")
                        print("\n")

        case "7":
            while True:
                print(" Deseja Recuperar :")
                print("1 - Biblioteca")
                print("2 - Pasta")
                print("3 - Foto")
                print("0 - Sair")
                balde = input("Escolha uma opção: ")
                match balde:

                    case "1":
                        print("Biblioteca:")
                        while True:
                            name_bibliotecas = input("Digite o nome da biblioteca: ")
                            if name_bibliotecas.strip() == "":
                                print("Nome inválido.")
                            else:
                                break
                        busca=None
                        for item in lixeira:
                            if item["tipo"] == "biblioteca" and item["biblioteca"] == name_bibliotecas :
                                busca =item
                                break
                        if busca == None:
                            print("Biblioteca não encontrada.")
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
                            else:
                                if name_bibliotecas in bibliotecas:
                                    print("Já existe uma biblioteca com esse nome. Não foi possível recuperar.")
                                else:
                                    bibliotecas[name_bibliotecas] = busca["conteudo"]

                                    lixeira.remove(busca)

                                    print("Biblioteca recuperada com sucesso.")
                    case "2":
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

                        busca=None
                        for item in lixeira:
                            if item["tipo"] == "pasta" and item["biblioteca"] == name_bibliotecas and item["nome"] == nome_pasta :
                                busca =item
                                break
                        if busca == None:
                            print("Arquivo não encontrado.")
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
                            else:
                                if name_bibliotecas not in bibliotecas:
                                    bibliotecas[name_bibliotecas] = {}
                                if nome_pasta in bibliotecas[name_bibliotecas]:
                                    print("Já existe uma pasta com esse nome. Não foi possível recuperar.")
                                else:
                                    bibliotecas[name_bibliotecas][nome_pasta] = busca["conteudo"]
                                    lixeira.remove(busca)

                                    print("Pasta recuperada com sucesso.")

                    case "3":
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

                        busca=None
                        for item in lixeira:
                            if item["tipo"] == "foto" and item["biblioteca"] == name_bibliotecas and item["pasta"]== nome_pasta and item["nome"] == foto :
                                busca =item
                                break
                        if busca == None:
                            print("Arquivo não encontrado.")
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
                            else:
                                if name_bibliotecas not in bibliotecas:
                                    bibliotecas[name_bibliotecas] = {}

                                if nome_pasta not in bibliotecas[name_bibliotecas]:
                                    bibliotecas[name_bibliotecas][nome_pasta] = []
                                if busca["nome"] in bibliotecas[name_bibliotecas][nome_pasta]:
                                    print("Essa foto já existe nessa pasta. Não foi possível recuperar.")
                                else:
                                    bibliotecas[name_bibliotecas][nome_pasta].append(busca["nome"])

                                    lixeira.remove(busca)

                                    print("Foto recuperada com sucesso.")
                    case "0":
                        # ==========================
                        # SAIR
                        # ==========================
                        print("Retornando ao Menu...")
                        break
                    case _:
                        print("Opção inválida.")
        case "0":
            # ==========================
            # SAIR
            # ==========================
            print("Encerrando o sistema...")
            break

        case _:
            print("Opção inválida.")