def somar(a, b):
    return a + b


def calcular_media(nota1, nota2, nota3):
    total = nota1 + nota2 + nota3
    return total / 3


def verificar_motociclista(nome, capacete, velocidade):
    if capacete == "Sim" and velocidade <= 60:
        return "Regular"
    else:
        return "Irregular"


resultado1 = somar(15, 20)
print(f"Soma: {resultado1}")

resultado2 = calcular_media(7, 7, 7)
print(f"Média: {resultado2}")

resultado3 = verificar_motociclista("Rubens", "Sim", 58)
print(f"Situação: {resultado3}")
