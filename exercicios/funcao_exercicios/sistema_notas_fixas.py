from exercicios.list_Exercicios.desafio7_dificil import total
from exercicios.tuplas_Exercicios.exercicio_medio import quantas_vezes

notas = (7, 8, 5, 10, 6, 9, 4, 8, 7, 10)


def mostrar_notas():
    for nota in notas:
        print(nota)


def exibir_primeira_nota():
    print(notas[0])


def exibir_ultima_nota():
    ultima_nota = (len(notas) - 1)
    print(notas[ultima_nota])


def maior_nota():
    maior = 0

    for nota in notas:
        if nota > maior:
            maior = nota

    print(maior)


def menor_nota():
    menor = 10

    for nota in notas:
        if nota < menor:
            menor = nota

    print(menor)


def media_notas():
    soma = 0
    for nota in notas:
        soma += nota
    media = (soma/len(notas))
    print(media)


def contar_nota_10():
    valor = 10
    notas.count(valor)
    print(notas)

maior_nota()
menor_nota()
media_notas()
contar_nota_10()