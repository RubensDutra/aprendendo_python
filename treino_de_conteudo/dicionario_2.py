estoque = {}


def adicionar_produto(nome, quantidade):
    estoque[nome] = quantidade


def remover_produto(nome_chave):
    del estoque[nome_chave]


def alterar_quantidade(nome, quantidade_nova):
    estoque[nome] = quantidade_nova


def listar():
    for k, v in estoque.items():
        print(f"{k} - {v}")


def consultar_estoque(consultar):
    for k, v in estoque.items():
        if consultar == k or consultar == v:
            print(f"{k} - {v}")
            return
    print("Produto não econtrado!")


adicionar_produto("A", 10)
adicionar_produto("B", 15)
adicionar_produto("C", 15)
listar()

print("-------------------------")
remover_produto("B")
listar()
print("-------------------------")
alterar_quantidade("C", 100)
listar()
print("-------------------------")
consultar_estoque(100)
