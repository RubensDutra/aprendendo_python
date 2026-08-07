pessoas = {'Nome': '', 'Idade': 0, 'Cidade': ''}

def adicionar_nome():
    pessoas['Nome'] = str(input('Nome: '))

def adicionar_idade():
    pessoas['Idade'] = int(input('Idade: '))

def adicionar_cidade():
    pessoas['Cidade'] = str(input('Cidade: '))

def exibir_informacao():
    for k, v in pessoas.items():
        print(f'{k} - {v}')

def alterar_cidade():
    nome_cidade = str(input('Cidade: '))

    for k, v in pessoas.items():
        if v == nome_cidade:
            novo_nome = str(input('Cidade: '))
            pessoas.update({'Cidade': novo_nome})
            break

def alterar_idade():
    idade = int(input('Idade: '))

    for k, v in pessoas.items():
        if v == idade:
            pessoas.pop(k)
            break


adicionar_nome()
adicionar_idade()
adicionar_cidade()
exibir_informacao()
alterar_cidade()
exibir_informacao()
alterar_idade()
exibir_informacao()