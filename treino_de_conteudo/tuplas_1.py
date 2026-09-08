from pip._internal import index

notas = (7.5, 8.2, 6.0, 9.1, 5.5)
disciplinas = ('Matemática', 'Português', 'História', 'Ciências', 'Inglês')


def media():
    return sum(notas) / len(notas)


def maior_nota():
    return max(notas)


def menor_nota():
    return min(notas)


def new_tuplas_com_notas_maior_que_7():
    tuplas = []
    for nota in notas:
        if nota >= 7:
            tuplas.append(nota)
    return tuplas


def disciplina_reprovadas(notas, disciplinas):
    for nota in notas:
        if nota >= 7:
            posicao = notas.index(nota)
            print(disciplinas[posicao])


def lista_de_materias_aprovadas():
    conta = 0
    for nota in notas:
        if nota < 7:
            conta += 1
    return conta

disciplina_reprovadas(notas, disciplinas)
