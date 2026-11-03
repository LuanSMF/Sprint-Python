import json
import os

arquivo = "dados.json"

def salvar_dados(dados):
    try:
        with open("dados.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4,ensure_ascii=False)
        print("Arquivo salvo com sucesso")
    except OSError as erro:
        print(f"Erro ao salvar o arquivo: {erro}")

def carregar_dados():
    if not os.path.exists("dados.json"):
        dados = {
            "bibliotecas": {},
            "lixeira": []
        }
        salvar_dados(dados)
        return dados
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)
