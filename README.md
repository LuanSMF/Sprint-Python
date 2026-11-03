# 📸 Organizer — Gerenciador de Fotos

O **Organizer** é um sistema desenvolvido em Python para organizar e gerenciar fotos digitais por meio de bibliotecas e pastas. A aplicação funciona através de um menu interativo no terminal e permite adicionar, visualizar, remover e recuperar conteúdos.

O projeto foi desenvolvido como parte da disciplina **Computational Thinking with Python — Sprint **, com foco na aplicação de conceitos de lógica de programação, estruturas de dados e modularização.

## 🎯 Objetivo

Oferecer uma maneira simples e organizada de gerenciar fotos digitais, mantendo uma estrutura hierárquica:

```text
Biblioteca
│
├── Pasta
│   ├── Foto 1
│   └── Foto 2
│
└── Pasta
    ├── Foto 3
    └── Foto 4
```

> As "fotos" são representadas pelo **nome** informado pelo usuário (por exemplo, `praia.jpg`). O sistema organiza esses nomes; ele não move nem copia arquivos de imagem reais.

## ⚙️ Funcionalidades

O menu principal oferece as seguintes opções:

| Opção | Funcionalidade | Descrição |
|---|---|---|
| 1 | Adicionar biblioteca | Cria uma nova biblioteca. Não permite nomes repetidos. |
| 2 | Adicionar pasta | Cria uma pasta dentro de uma biblioteca existente. |
| 3 | Adicionar fotos em uma pasta | Adiciona uma foto a uma pasta existente. Não permite nomes repetidos na mesma pasta. |
| 4 | Ver bibliotecas | Exibe todas as bibliotecas, pastas e fotos cadastradas. |
| 5 | Transferir para lixeira | Envia uma biblioteca, uma pasta ou uma foto para a lixeira, com confirmação. |
| 6 | Ver lixeira | Lista os itens removidos e o caminho de origem de cada um. |
| 7 | Recuperar da lixeira | Restaura uma biblioteca, uma pasta ou uma foto, com confirmação. |
| 8 | Buscar imagem online | Baixa uma imagem aleatória (400x300) do serviço [Lorem Picsum](https://picsum.photos) e salva como `image.jpg` na pasta onde o programa foi executado. |
| 0 | Sair | Encerra o sistema. |

### Como funciona a lixeira

- **Envio para a lixeira:** se já existir na lixeira um item com o mesmo nome (e mesmo local de origem), o novo item recebe um sufixo numérico, como `Viagens (1)`, para que nenhum seja sobrescrito.
- **Recuperação de biblioteca ou pasta:** se o destino já existir, o conteúdo recuperado é **mesclado** ao existente, sem duplicar fotos.
- **Recuperação de foto:** se a foto já existir na pasta de destino, a recuperação é recusada. Se a biblioteca ou a pasta de origem não existirem mais, elas são recriadas.
- **Itens renomeados:** para recuperar um item que recebeu sufixo, digite o nome **com o sufixo**, exatamente como aparece na opção "Ver lixeira". Uma biblioteca recuperada volta com o nome digitado.
- **Permanência:** a lixeira não possui exclusão definitiva. Os itens permanecem nela até serem recuperados.

## 🛠️ Tecnologias e conceitos utilizados

- Python 3.10 ou superior (o projeto usa `match/case`).
- Biblioteca externa [`requests`](https://pypi.org/project/requests/) para a requisição HTTP.
- JSON para persistência dos dados.
- Listas e dicionários.
- Funções e modularização.
- Estruturas condicionais (`if`, `elif`, `else`, `match/case`).
- Estruturas de repetição (`while` e `for`).
- Manipulação de arquivos.
- Validação de entradas do usuário.
- Tratamento de exceções (`try/except`) para JSON corrompido ou incompleto, erros de leitura e escrita de arquivos, falhas de rede e interrupção por `Ctrl+C`.

## 📂 Estrutura do projeto

O código é dividido em módulos, separando as responsabilidades de cada funcionalidade:

```text
Organizer/
│
├── main.py
├── adicionar.py
├── auxiliar.py
├── consulta.py
├── lixeira.py
├── permanencia.py
├── transf.py
│
├── dados.json        (criado automaticamente na primeira execução)
├── image.jpg         (criada ao usar a opção 8)
│
└── README.md
```

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Inicialização, menu principal e tratamento de erros gerais. |
| `adicionar.py` | Criação de bibliotecas, pastas e adição de fotos. |
| `auxiliar.py` | Validação das entradas do usuário, pedido de confirmação e exibição das bibliotecas. |
| `consulta.py` | Download de uma imagem aleatória pela internet (`requests`). |
| `lixeira.py` | Visualização da lixeira e recuperação de bibliotecas, pastas e fotos. |
| `permanencia.py` | Carregamento e salvamento dos dados em `dados.json`. |
| `transf.py` | Transferência de bibliotecas, pastas e fotos para a lixeira. |
| `dados.json` | Armazenamento persistente das informações. |

## 💾 Persistência de dados

O Organizer utiliza um arquivo `dados.json` para manter as informações mesmo depois que o programa é encerrado. Se o arquivo não existir, ele é criado automaticamente na primeira execução. Os dados são salvos após cada alteração.

Os dados são organizados em duas estruturas principais:

- `bibliotecas`: armazena as bibliotecas, suas pastas e respectivas fotos.
- `lixeira`: armazena os itens removidos. Cada item tem um `tipo` (`biblioteca`, `pasta` ou `foto`) e campos que indicam sua origem.

Exemplo da estrutura:

```json
{
    "bibliotecas": {
        "Minha Biblioteca": {
            "Viagens": [
                "praia.jpg",
                "montanha.jpg"
            ]
        }
    },
    "lixeira": [
        {
            "tipo": "foto",
            "biblioteca": "Minha Biblioteca",
            "pasta": "Viagens",
            "nome": "cidade.jpg"
        },
        {
            "tipo": "pasta",
            "biblioteca": "Minha Biblioteca",
            "nome": "Família",
            "conteudo": ["natal.jpg", "aniversario.jpg"]
        },
        {
            "tipo": "biblioteca",
            "biblioteca": "Trabalho",
            "nome_original": "Trabalho",
            "conteudo": {
                "Eventos": ["palestra.jpg"]
            }
        }
    ]
}
```

Se o `dados.json` estiver corrompido ou incompleto, o programa informa o erro e não inicia, evitando a perda de dados.

## ▶️ Como executar

**1.** Instale o **Python 3.10 ou superior** em seu computador.

**2.** Faça o download ou clone este repositório:

```bash
git clone URL_DO_REPOSITORIO
```

**3.** Entre na pasta do projeto:

```bash
cd Organizer
```

**4.** Instale a dependência:

```bash
pip install requests
```

**5.** Execute o programa:

```bash
python main.py
```

O menu principal será exibido no terminal, permitindo navegar pelas funcionalidades disponíveis. A opção 8 (buscar imagem online) exige conexão com a internet.

## 👥 Equipe — IRIS

Projeto desenvolvido pela equipe IRIS:

- Manuella Thomazini
- João Nóbrega
- Kevin Simões
- Luan Sá
- Flávia Camerim

**Instituição:** FIAP  
**Disciplina:** Computational Thinking with Python  
**Projeto:** Sprint — Organizer

---

*Organizer: organização simples, prática e estruturada para suas fotos digitais.*
