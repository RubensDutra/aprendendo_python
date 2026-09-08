dicionaro_alunos = {}


def cadastrar_aluno(matricula, nome, idade, curso, nota):
    dicionaro_alunos[matricula] = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "nota": nota
    }


def alterar_nota(matricula, nova_nota):
    dicionaro_alunos[matricula]['nota'] = nova_nota


def listar_alunos():
    for k, v in dicionaro_alunos.items():
        print(f'{k}: {v["nome"]} | {v["idade"]} | {v["curso"]}| {v["nota"]}')


def verificar_notas():
    for k, v in dicionaro_alunos.items():
        if v["nota"] >= 7:
            print(f"{k}: Nome: {v['nome']} - Nota: {v['nota']}")


def buscar_informacao(buscar):
    for k, v in dicionaro_alunos.items():
        if (
                k == buscar or
                v["nome"] == buscar or
                v["idade"] == buscar or
                v["curso"] == buscar or
                v["nota"] == buscar):
            print(f"{k} - Nome: {v['nome']} - Nota: {v['nota']}"

                  )


cadastrar_aluno(125, "A", 25, 'ADS', 1.5)
cadastrar_aluno(321, "B", 27, 'ADS', 10)
cadastrar_aluno(258, "C", 18, 'ADS', 2)

buscar_informacao(25)
