## Criação do aquivo 'motociclista.txt'
arquivo = open('motociclista.txt', 'w')


def adicionar(nome, marca, modelo, ano):
    arquivo.write(f"nome:{nome} "
                  f"marca:{marca} "
                  f"modelo:{modelo} "
                  f"ano:{ano};\n")



adicionar("B", "Honda", 'CG', 2025)
adicionar("A", "Honda", 'CG', 2025)
adicionar("c", "Honda", 'CG', 2025)
