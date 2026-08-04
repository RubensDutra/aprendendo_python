lista = {}

def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    lista['nome:'] = nome

    preco = input("Digitar preço do produto: ")
    lista['preco:'] = preco

    quantidade = input("Digite o quantidade de produtos: ")
    lista['quantidade:'] = quantidade


def imprimir_produtos():

    print("======== PRODUTOS =======")

    for k, v in lista.items():
        print(f"{k} {v}")

    linha()


def linha():
    print("=======================")


cadastrar_produto()
imprimir_produtos()
