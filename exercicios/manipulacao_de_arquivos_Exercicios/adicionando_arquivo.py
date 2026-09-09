arquivo = open("motociclista.txt", "a")


def adicionar(capacete, velocidade):
    arquivo.write(f"capacete: {capacete}"
                  f", velocidade:{velocidade}\n")

adicionar("Sim", "80 Km/h")