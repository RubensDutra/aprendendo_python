## Criando arquivo, ou seja, escrevendo com write
arquivo = open('nomes.txt', "w")

arquivo.write("Rubens\n")
arquivo.write("Dutra\n")
arquivo.write("Mesquita\n")

## Fechando aquivo com close
arquivo.close()

## Adicionando um elemento no final do arquivo com modo "a"
arquivo = open('nomes.txt', "a")

arquivo.write("Kezia\n")
arquivo.close()

## Fechando aquivo com close
arquivo.close()

## Lendo aquivo no modo "r"
arquivo = open('nomes.txt', "r")

## Listando elemento do arquivos
for nome in arquivo:
    print(nome)
