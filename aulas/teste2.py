def receber_nome(nome):
    return nome


def verificar_idade(idade):
    if idade >= 18:
        return True
    else:
        return False


def verificar_capacete(capacete):
    if capacete == "Sim":
        return True
    else:
        return False


def verificar_velocidade(velocidade):
    if velocidade <= 60:
        return True
    else:
        return False


def determinar_situacao(nome, idade, capacete, velocidade):

    if verificar_idade(idade) and verificar_capacete(capacete) and verificar_velocidade(velocidade):
        print(f"Motociclista {receber_nome(nome)}, estar REGULAR!")
    else:
        print(f"Motociclista {receber_nome(nome)}, estar IRREGULAR!")


determinar_situacao("Rubens", 26, "Sim", 60)
