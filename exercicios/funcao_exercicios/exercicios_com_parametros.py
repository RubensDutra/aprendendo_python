def mostrar_nome(nome):
    print(f"Nome:{nome}")


def apresentar_produto(nome, preco, quantidade):
    print(f"Nome: {nome}")
    print(f"Preço: {preco}")
    print(f"Quantidade: {quantidade}")


def verificar_motociclista(nome, capacete, velocidade):
    print(f"Motociclica: {nome}")
    print(f"Capacete: {capacete}")
    print(f"Velocidade: {velocidade} km")

    if capacete == "Sim" and velocidade <= 60:
        print("Situação: Regular")
    else:
        print("Situação: Irregular")


mostrar_nome("Rubens")

print("========= PRODUTO =======")
apresentar_produto("Arroz", 15, 10)

verificar_motociclista("Rubens", "Não", 55)
