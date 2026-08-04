motociclistas = {}


def capturar_motociclista():
    nome = input("Digite o nome do motociclica")
    motociclistas["Motociclica"] = nome

    capacete = input("De capacete? ")
    motociclistas["Capacete"] = capacete

    velocidade = int(input("Qual a velocidade? "))
    motociclistas["Velocidade"] = velocidade


def verificar_capacete():

    if motociclistas["Capacete"] == 'Sim':
        motociclistas["Capacete"] = True
    else:
        motociclistas["Capacete"] = False


def verificar_velocidade():

    if motociclistas["Velocidade"] > 60:
        motociclistas['Status'] = 'Acima da velocidade'
    else:
        motociclistas['Status'] = 'Velocidade permitida'


def imprimir_dados():

    print("\n======= DADOS DO MOTOCICLISTA =======")

    for k, v in motociclistas.items():
        print(f"{k} - {v}")


capturar_motociclista()
verificar_capacete()
verificar_velocidade()
imprimir_dados()
