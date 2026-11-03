from auxiliar import digitar_nome_pasta, digitar_nome_bibliotecas, digitar_nome_fotos
from permanencia import salvar_dados
def criar_bibliotecas(bibliotecas,dados):
    
    name_bibliotecas=digitar_nome_bibliotecas()

    if (name_bibliotecas in bibliotecas):
        print("Biblioteca já existe!")
        return False
    else:
        bibliotecas[name_bibliotecas] = {}
        salvar_dados(dados)
        print("Biblioteca criada com sucesso!")
        return True

def criar_pasta(bibliotecas,dados):
    
    name_bibliotecas=digitar_nome_bibliotecas()

    if (name_bibliotecas not in bibliotecas):
        print("Biblioteca não encontrada")
        return False
    else:
        nome_pasta=digitar_nome_pasta()
        if (nome_pasta in bibliotecas[name_bibliotecas]):
            print("Pasta já existe!")
            return False
        else:
            bibliotecas[name_bibliotecas][nome_pasta] = []
            salvar_dados(dados)
            print("Pasta criada com sucesso!")
            return True

def adicionar_fotos(bibliotecas,dados):
    name_bibliotecas=digitar_nome_bibliotecas()
    if (name_bibliotecas not in bibliotecas):
        print("Biblioteca não encontrada.")
        return False
    else:
        nome_pasta=digitar_nome_pasta()
        if (nome_pasta not in bibliotecas[name_bibliotecas]):
            print("Pasta não encontrada.")
            return False
        else:
            foto = digitar_nome_fotos()
            if foto in bibliotecas[name_bibliotecas][nome_pasta]:
                print("Essa foto já existe nessa pasta.")
                return False
            else:
                bibliotecas[name_bibliotecas][nome_pasta].append(foto)
                salvar_dados(dados)
                print("Foto Adicionada com sucesso!")
                return True