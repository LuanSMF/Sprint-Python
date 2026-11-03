from auxiliar import confirmacao,digitar_nome_bibliotecas,digitar_nome_pasta,digitar_nome_fotos
from permanencia import salvar_dados
def transferir(bibliotecas,lixeira,dados):
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
                transferir_bibliotecas(bibliotecas,lixeira,dados)
                return
            case "2":
                transferir_pasta(bibliotecas,lixeira,dados)
                return
            case "3":
                transferir_fotos(bibliotecas,lixeira,dados)
                return
            case "0":
                # ==========================
                # SAIR
                # ==========================
                print("Fechando lixeira.")
                return

            case _:
                print("Opção inválida.")

def transferir_bibliotecas(bibliotecas,lixeira,dados):
    name_bibliotecas=digitar_nome_bibliotecas()
    if name_bibliotecas not in bibliotecas:
        print("Biblioteca não encontrada.")
        return False
    else:
        resposta = confirmacao()
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
            conteudo = bibliotecas.pop(name_bibliotecas)
            lixeira.append({
                "tipo": "biblioteca",
                "biblioteca": nome_final,
                "nome_original": name_bibliotecas,
                "conteudo": conteudo
            })
            salvar_dados(dados)
            print("Biblioteca enviada para lixeira.")
            return True

def transferir_pasta(bibliotecas,lixeira,dados):
    
    name_bibliotecas = digitar_nome_bibliotecas()

    if name_bibliotecas not in bibliotecas:
        print("Biblioteca não encontrada.")
        return False

    else:
        nome_pasta = digitar_nome_pasta()

        if nome_pasta not in bibliotecas[name_bibliotecas]:
            print("Pasta não encontrada.")
            return False

        resposta = confirmacao()

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
            conteudo = bibliotecas[name_bibliotecas].pop(nome_pasta)
            lixeira.append({
                "tipo": "pasta",
                "biblioteca": name_bibliotecas,
                "nome": nome_final,
                "conteudo": conteudo
            })
            salvar_dados(dados)
            print("Pasta enviada para lixeira.")
            return True

def transferir_fotos(bibliotecas,lixeira,dados):
    name_bibliotecas=digitar_nome_bibliotecas()
    if name_bibliotecas not in bibliotecas:
        print("Biblioteca não encontrada.")
        return False

    else:
        
        nome_pasta=digitar_nome_pasta()

        if nome_pasta not in bibliotecas[name_bibliotecas]:
            print("Pasta não encontrada.")
            return False

        else:
            
            foto=digitar_nome_fotos()

            if foto not in bibliotecas[name_bibliotecas][nome_pasta]:
                print("Foto não encontrada.")
                return False

            resposta = confirmacao()

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
                salvar_dados(dados)
                print("Foto enviada para lixeira.")
                return True