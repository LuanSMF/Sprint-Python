import requests

def buscar_imagem():
    try:
        print("Buscando imagem...")

        url = "https://picsum.photos/400/300"

        resposta=  requests.get(url,timeout=15)

        print("Status:", resposta.status_code)

        if  resposta.status_code == 200:
            with open("image.jpg", "wb") as arquivo:
                arquivo.write(resposta.content)
            print("Imagem adicionado com sucesso!")
        else:
            print("Erro ao  buscar imagem")
    except requests.exceptions.RequestException as erro:
        print("Erro:", erro)