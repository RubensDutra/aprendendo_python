dias = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")


def mostrar_dias():
    for dia in dias:
        print(dia)


def mostrar_primeiro_dia():
    print(dias[0])


def mostrar_ultimo_dia():
    print(len(dias) - 1)


def escolher_dia():
    posicao_indice = dias.count(input('Digite o nome do dia: '))

    if posicao_indice != 0:
        print(f"{dias[posicao_indice]} existe!")
    else:
        print("Não existe")


def mostrar_posicao():
    print(dias.index(input('Digite o nome do dia: ')))


def total_dias():
    total = len(dias)
    print(total)

total_dias()
escolher_dia()
mostrar_posicao()
