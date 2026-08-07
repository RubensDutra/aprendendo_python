notas = [8, 9, 1, 3, 7, 5, 9, 10]


def mostrar_notas():
    for nota in notas:
        print(nota)


def maior_nota():
    maior = 0

    for nota in notas:
        if nota > maior:
            maior = nota

    return maior


def menor_nota():
    menor = 10

    for nota in notas:

        if nota < menor:
            menor = nota

    return menor


def media_nota():
    total = 0
    for nota in notas:
        total += nota

    return total / len(notas)


def total_notas_maior_ou_igual_7():
    total = 0
    for nota in notas:
        if nota >= 7:
            total += 1

    return total


def total_notas_menor_que_7():
    total = 0
    for nota in notas:
        if nota < 7:
            total += 1

    return total


def notas_em_ordem_crescente():
    notas.sort(reverse=False)

    for nota in notas:
        print(nota)


mostrar_notas()
print(f"Maior nota: {maior_nota()}")
print(f"Menor nota: {menor_nota()}")
print(f"Média: {media_nota()}")
print(f"Total de notas igual ou maior que 7: {total_notas_maior_ou_igual_7()}")
print(f"Total de notas menor que 7: {total_notas_menor_que_7()}")
notas_em_ordem_crescente()
