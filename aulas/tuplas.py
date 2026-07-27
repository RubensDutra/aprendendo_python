# Sintaxe da tuplas
cores = ("verde", "amarelo", "azul")

# Acessando valores por indices
print("====== Acessando indices======")
print(cores[0], cores[1], cores[2])

# Acessando indices negativos do List
print(cores[-0], cores[-1], cores[-2])

# Descobrindo o tamanho da tupla usando a função len()
print(len(cores))

# Metodos da tupla
 # - count
total = cores.count("verde")
print(total)

# - index
posicao = cores.index("verde")
print(posicao)


