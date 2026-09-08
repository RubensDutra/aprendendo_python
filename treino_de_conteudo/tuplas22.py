estoque = (
    ("Caneta", 2.50, 120),
    ("Caderno", 15.90, 45),
    ("Mochila", 89.90, 8),
    ("Lápis", 1.20, 200),
    ("Borracha", 1.80, 150),
    ("Estojo", 25.00, 0),
    ("Régua", 3.50, 60),
)


def calcular_estoque():
    total = 0
    for produto in estoque:
        total += produto[1] * produto[2]
    return total


def produto_mais_caro():
    produto = max(estoque, key=lambda item: item[1])
    return produto


def produto_mais_barato():
    valor = 1236547
    nome = ''
    for nome, preco, quantidade in estoque:
        if preco < valor:
            valor = preco
            nome = nome
    return nome


print(produto_mais_caro())
