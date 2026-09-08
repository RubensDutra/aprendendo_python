matriz = []


def gerar():
    for i in range(5):
        linha = []
        for j in range(5):
            linha.append((j + 1) + i)
        matriz.append(linha)


def imprimir():
    for i in range(5):
        for j in range(5):
            print(f'[{matriz[i][j]:^5}]', end='')
        print()


gerar()
imprimir()
