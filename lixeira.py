from auxiliar import digitar_nome_pasta,digitar_nome_bibliotecas,digitar_nome_fotos,confirmacao
from permanencia import salvar_dados
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

def recuperar_lixeira(bibliotecas,lixeira,dados):
    while True:
        print(" Deseja Recuperar :")
        print("1 - Biblioteca")
        print("2 - Pasta")
        print("3 - Foto")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")
        match opcao:

            case "1":
                recuperar_bibliotecas(bibliotecas, lixeira,dados)
                return
            case "2":
                recuperar_pasta(bibliotecas, lixeira,dados)
                return
            case "3":
                recuperar_foto(bibliotecas, lixeira,dados)
                return
            case "0":
                # ==========================
                # SAIR
                # ==========================
                print("Retornando ao Menu...")
                return
            case _:
                print("Opção inválida.")

def recuperar_bibliotecas(bibliotecas,lixeira,dados):
    print("Biblioteca:")
    name_bibliotecas=digitar_nome_bibliotecas()
    busca = None
    for item in lixeira:
        if item["tipo"] == "biblioteca" and item["biblioteca"] == name_bibliotecas:
            busca = item
            break
    if busca == None:
        print("Biblioteca não encontrada.")
        return False
    else:

        resposta = confirmacao()

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
            salvar_dados(dados)
            print("Biblioteca recuperada com sucesso.")

            return True

def recuperar_pasta(bibliotecas,lixeira,dados):
    print("Pasta:")
    name_bibliotecas=digitar_nome_bibliotecas()
    nome_pasta=digitar_nome_pasta()
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

        resposta = confirmacao()

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
            salvar_dados(dados)
            print("Pasta recuperada com sucesso.")
            return True

def recuperar_foto(bibliotecas,lixeira,dados):
    print("Foto:")
    
    name_bibliotecas=digitar_nome_bibliotecas()

    nome_pasta=digitar_nome_pasta()

    foto=digitar_nome_fotos()

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

        resposta = confirmacao()

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
                salvar_dados(dados)

                print("Foto recuperada com sucesso.")
                return True