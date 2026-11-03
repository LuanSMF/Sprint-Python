import json
from adicionar import criar_bibliotecas,criar_pasta,adicionar_fotos
from auxiliar import ver_bibliotecas
from transf import transferir
from lixeira import ver_lixeira,recuperar_lixeira
from consulta import buscar_imagem
from permanencia import carregar_dados

def carregar():
    try:
        dados = carregar_dados()
        dados["bibliotecas"], dados["lixeira"]
        return dados
    except json.JSONDecodeError:
        print("Erro: o arquivo dados.json está corrompido.")
    except (KeyError,TypeError):
        print("Erro: o arquivo dados.json está incompleto.")
    except OSError as erro:
        print(f"Erro ao ler o arquivo de dados: {erro}")
    return None
def main ():
    dados = carregar()
    if dados is None:
        return
    bibliotecas = dados["bibliotecas"]
    lixeira = dados["lixeira"]
    while(True):
        try:
            print("\n===== MENU =====")
            print("1 - Adicionar biblioteca")
            print("2 - Adicionar pasta")
            print("3 - Adicionar fotos em uma pasta")
            print("4 - Ver bibliotecas")
            print("5 - Transferir para lixeira")
            print("6 - Ver lixeira")
            print("7 - Recuperar da Lixeira")
            print("8 - Buscar imagem online")
            print("0 - Sair")

            menu = input("Escolha uma opção: ").strip()

            match menu:
                    case "1":
                        # ADICIONAR BIBLIOTECA
                        criar_bibliotecas(bibliotecas,dados)
                    case "2":
                        # ADICIONAR PASTA
                        criar_pasta(bibliotecas,dados)
                    case "3":
                        adicionar_fotos(bibliotecas,dados)
                    case "4":
                        ver_bibliotecas(bibliotecas)
                    case "5":
                        transferir(bibliotecas,lixeira,dados)
                    case "6":
                        ver_lixeira(lixeira)
                    case "7":
                        recuperar_lixeira(bibliotecas,lixeira,dados)
                    case "8":
                        buscar_imagem()
                    case "0":
                        # ==========================
                        # SAIR
                        # ==========================
                        print("Encerrando o sistema...")
                        break

                    case _:
                        print("Opção inválida.")
        except (KeyboardInterrupt, EOFError):
            print("\nOperação interrompida. Encerrando o sistema...")
            return
        except OSError as erro:
            print(f"Erro ao acessar arquivo: {erro}. Voltando ao menu.")
        except (KeyError, ValueError) as erro:
            print(f"Erro nos dados ({erro!r}). Voltando ao menu.")

if __name__ == "__main__":
    main()