carro = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "ano": 2020
}
print(carro)

carro["ano"] = 2024
print(carro)

carro.update({"cor":"prata"})
print(carro)

del carro["cor"]
print(carro)