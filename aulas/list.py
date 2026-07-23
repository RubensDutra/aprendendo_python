# Sintaxe do List
nomes = ["Rubens", "Robson", "Guilherme"]
notas = [10, 8.5, 9.0]
idades = [26, 24, 12]

# Acessando indices do List
print("====== Acessando indices ")
print(nomes[0])
print(notas[1])
print(idades[2])

# Acessando indices negativos do List
print(nomes[-0])
print(notas[-1])
print(idades[-2])

# Descobrindo o tamanho do list usando a função len()
print(len(nomes))
print(len(notas))
print(len(idades))

# Percorrendo uma List
for nome in nomes:
    print(nome)
