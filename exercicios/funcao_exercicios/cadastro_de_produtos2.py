# Lista
produtos = []

# Tuplas
categorias_produtos = ("Eletrônico", "Alimento", "Vestimenta")


def cadastrar_produtos():
    # Diretorio
    informacoes_produtos = {}

    nome = input("Qual o nome do produto? ")
    informacoes_produtos["nome"] = nome

    preco = float(input("Qual o valor do produto? R$ "))
    informacoes_produtos["preco"] = preco

    quantidade = int(input("Quantos produtos deseja cadastrar? "))
    informacoes_produtos["quantidade"] = quantidade

    menu_categoria()

    opcao_cadastro = int(input("Qual categoria deseja cadastrar? "))

    if opcao_cadastro == 1:
        informacoes_produtos["categoria"] = categorias_produtos[0]
    elif opcao_cadastro == 2:
        informacoes_produtos["categoria"] = categorias_produtos[1]
    else:
        informacoes_produtos["categoria"] = categorias_produtos[2]

    produtos.append(informacoes_produtos)


def menu_categoria():
    print("\n====== MENU CATEGORIAS ======")
    print("1 -", categorias_produtos[0])
    print("2 -", categorias_produtos[1])
    print("3 -", categorias_produtos[2])

def listar_produtos():
    for produto in produtos:
        print(f"Produto: {produto['nome']} | "
              f"Preço: {produto['preco']} | "
              f"Quantidade: {produto['quantidade']} | "
              f"Categoria: {produto['categoria']}"
              )


def listar_produtos_por_quantidade():
    for produto in produtos:
        if produto['quantidade'] > 0:
            print(f"Produto: {produto['nome']} | "
                  f"Preço: {produto['preco']} | "
                  f"Quantidade: {produto['quantidade']} | "
                  f"Categoria: {produto['categoria']}"
                  )



