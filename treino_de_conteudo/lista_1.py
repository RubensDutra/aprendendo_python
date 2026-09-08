notas = [2.5, 6.7, 10, 8, 10, 7]


def adicionar_notas(nota):
    if nota < 0:
        print("Nota invalida!")
        return

    notas.append(nota)


def calcular_media():
    if len(notas) == 0:
        print("Lista vazia!")
        return

    qnt = len(notas)
    total_notas = 0

    for nota in notas:
        total_notas += nota

    media = total_notas / qnt
    return media


def maior_nota():
    if len(notas) == 0:
        print("Lista vazia!")
        return None

    maior = -216346189984

    for nota in notas:
        if nota > maior:
            maior = nota

    return maior


def menor_nota():
    if len(notas) == 0:
        print("Lista vazia!")
        return None

    menor = 216346189984

    for nota in notas:
        if nota < menor:
            menor = nota

    return menor


def listar_aprovados():
    if len(notas) == 0:
        print("Lista vazia!")
        return None

    aprovados = []

    for nota in notas:
        if nota >= 7:
            aprovados.append(nota)

    return aprovados


