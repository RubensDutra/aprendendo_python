# Sintaxe da função
def exibir_mensagem():
    print("Olá, mundo!")

# Sintaxe da função com varios Parâmetros
def apresentar_produto(nome, preco, quantidade):
    print(f"Nome: {nome}")
    print(f"Preço: {preco}")
    print(f"Quantidade: {quantidade}")

# Função sem return
def somar(a, b):
    print(a + b)

# Função com return
def somar2(a, b):
    return a + b

# Função com valor padrão para idade
def apresentar(nome, idade = 18):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")

#Chamando a função apresentar sem passar o valor no parâmetro idade
apresentar("Rubens")

#Chamando a função apresentar passando o valor no parâmetro idade
apresentar("Ana", 28)

resulatdo = somar(10, 20)
print(resulatdo)

print("========================")

resulatdo = somar2(10, 20)
print(resulatdo)

# def -> Palavra reservada que cria uma função
# exibir_mensagem -> Nome da função
# () -> Parênteses (onde passamos parâmetros)
# : -> Inicio do bloco da função
# corpo da função -> Código que será executado
