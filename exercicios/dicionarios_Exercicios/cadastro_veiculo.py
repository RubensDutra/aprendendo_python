carro = {
    "marca": "",
    "modelo": "",
    "ano": 0,
    "preco": 0.0,
    "cor": ""
}


def adicionar_veiculo():
    carro["marca"] = input("Informe o nome do carro: ")
    carro["modelo"] = input("Informe o nome do modelo: ")
    carro["ano"] = int(input("Informe o ano: "))
    carro["preco"] = float(input("Informe valor do carro:"))
    carro["cor"] = input("Informe o cor do carro: ")

def exibir_informacao():
    for k, v in carro.items():
        print(f"{k} - {v}")


def menu():
    print(f"1 - Marca")
    print("2 - Modelo")
    print("3 - Ano")
    print("4 - Preço")
    print("5 - Cor")


def alterar_informacao():
    menu()
    opcao = int(input("Informe uma opcao: "))

    if opcao == 1:
        carro.update({"marca": input("Informe o nome do carro: ")})
    elif opcao == 2:
        carro.update({"modelo": input("Informe o nome do modelo: ")})
    elif opcao == 3:
        carro.update({"ano": int(input("Informe o ano do carro: "))})
    elif opcao == 4:
        carro.update({"preco": float(input("Informe o preço do carro: "))})
    elif opcao == 5:
        carro.update({"cor": input("Informe o cor do carro: ")})
    elif opcao > 5 or opcao < 1:
        print("Opção invalida!")

def remover_informacao():
    opcao = str(input("Deseja remover alguma informacão, Sim ou Não ?"))

    if opcao == "Sim":
        nome = input("Informe o que deseja excluir do carro:")
        carro.pop(nome)
    else:
        print("Sem alteração")

adicionar_veiculo()

print("===== Exibir ======")
exibir_informacao()

print("======== ALTERAR =======")
alterar_informacao()
exibir_informacao()

remover_informacao()
exibir_informacao()
