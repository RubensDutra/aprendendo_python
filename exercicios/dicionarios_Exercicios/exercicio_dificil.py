produto = {
    "nome": "arroz",
    "preço": 5.99,
    "estoque": 10,
    "categoria": "alimentos"
}

print(produto)

produto["preço"] = 10
print(produto)

produto["marca"] = "tio oliveira"
print(produto)

del produto["estoque"]
print(produto)

for k, v in produto.items():
    print(f"{k}: {v}")
