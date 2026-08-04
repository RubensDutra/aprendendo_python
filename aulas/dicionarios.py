# Sintaxe do dicionário
pessoa = {
    "nome": "Rubens",
    "idade": 30,
    "cidade": "Duque Bacelar"
}

# Acessando valores
print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["cidade"])

# Adicionar uma nova informação
pessoa["altura"] = 1.78
print(pessoa)

# Removendo uma informação
del pessoa["altura"]
print(pessoa)

# Percorrendo apenas chaves
for k in pessoa:
    print(k)

# Percorrendo chaves e valores
for k, v in pessoa.items():
    print(f"{k} - {v}")
