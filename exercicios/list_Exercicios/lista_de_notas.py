notas = [10, 6, 8, 3, 7]
notas_maior_7 = []
notas_menor_7 = []

for nota in notas:
    print(nota)

    if nota >= 7:
        notas_maior_7.append(nota)
    else:
        notas_menor_7.append(nota)

print("====== Notas maiores que 7 ===== ")
for nota in notas_maior_7:
    print(nota)

print("====== Notas menores que 7 ===== ")
for nota in notas_menor_7:
    print(nota)
