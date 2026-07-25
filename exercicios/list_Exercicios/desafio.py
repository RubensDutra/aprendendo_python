equipamentos = ["Notebook", "Mouse", "Teclado", "Monitor"]

nome = input("Qual equipamento deseja comprar: ")

is_exist = nome in equipamentos

if is_exist:
    print("Equipamento encontrado!")
else:
    print("Equipamento não encontrado!")
