produtos = ['A', 'B', 'C', 'D', 'E', 'F', 'G']


def adicionar_produto(nome):
    produtos.append(nome)


def remover_produto(nome):
    if len(produtos) == 0:
        print("Lista vazia!")
        return

    produtos.remove(nome)


def buscar_produtos(nome):

    if len(produtos) == 0:
        print("Lista vazia!")
        return

    status = nome in produtos

    if status:

        indice = produtos.index(nome)

        print(f'{produtos[indice]}')
    else:
        print("Produto não encontrado!")

def listar_produtos():
    if len(produtos) == 0:
        print("Lista vazia!")
        return
    for produto in produtos:
        print(produto)

def contar_produtos():
    if len(produtos) == 0:
        print("Lista vazia!")

    return len(produtos)


buscar_produtos('A')

print(contar_produtos())