compras = []


def cadastrar_produtos():
    valor = 0
    while 5 != valor:
        compras.append(input('Digite o nome do produto: '))
        valor = (valor + 1)

def mostrar_primeiro_produto():
    print(compras[0])


def mostrar_ultimo_produto():
    ultimo = (len(compras) - 1)
    print(compras[ultimo])


def total_de_produtos():
    total = len(compras)
    print(f'Total de produtos: {total}')

def remover_produto():
    nome_produto = input('Digite o nome do produto: ')
    compras.pop(compras.index(nome_produto))

def remover_produto_com_remover():
    nome_produto = input('Digite o nome do produto: ')
    compras.remove(nome_produto)

def mostrar_produtos():
    for produto in compras:
        print(produto)

cadastrar_produtos()
mostrar_primeiro_produto()
mostrar_ultimo_produto()
total_de_produtos()
remover_produto()
remover_produto_com_remover()
mostrar_produtos()
