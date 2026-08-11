def produto(nome, preco, quantidade):
    print(f"Nome: {nome}")
    print(f"Preço: {preco}")
    print(f"Quantidade: {quantidade}")


def calcular_total(preco, quantidade):
    return preco * quantidade


def verificar_estoque(quantidade):
    if quantidade > 0:
        return "Disponivel"
    else:
        return "Indisponivel"


def exibir_informacao():
    nome = input("Digitar nome do produto: ")
    preco = float(input("Digitar valor do produto: R$ "))
    quantidade = int(input("Digitar quantidade de itens: "))

    produto(nome, preco, quantidade)

    calcular = calcular_total(preco, quantidade)
    print(f"Total: R$ {calcular}")

    status = verificar_estoque(quantidade)
    print(f"Status:{status} ")


exibir_informacao()
