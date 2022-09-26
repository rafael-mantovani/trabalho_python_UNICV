aluno = []
def opcoes(aluno):
    print('1 - Cadastrar')
    print('2 - Listar')
    print('3 - Editar')
    print('4 - Deletar')
    print('5 - Sair')
    print('------------\n')

    opcao = int(input('Informe a Opção: '))
    if opcao == 1:
        cadastrar(aluno)
    elif opcao == 2:
        listar(aluno)
    elif opcao == 3:
        editar(aluno)
    elif opcao == 4:
        deletar(aluno)
    elif opcao == 5:
        sair(aluno)

    else:
        print('\nOpção inválida!')
        return opcoes(aluno)



#-----FUNÇÃO PARA CADASTRAR ALUNO------
def cadastrar(aluno):
    print('\n--- Cadastrar Aluno ---')
    id = int(input('Id: '))
    cpf = input('Cpf: ')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    turma = input('Turma: ')


    aluno.append({
        'id': id,
        'cpf': cpf,
        'nome': nome,
        'idade': idade,
        'turma': turma

    })
    print('-----------------------\n')
    print('Cadastro concluído!')

    opcao = int(input ('\nDeseja cadastrar um novo aluno? [1-Sim/2-Não]: '))
    if opcao == 1:
        cadastrar(aluno)

    elif opcao == 2:
        opcoes(aluno)

    else:
        print('\nOpção inválida!')
        opcoes(aluno)

#-------FUNÇÃO PARA LISTAR ALUNOS, COM OPÇÕES DE EDIT E DEL---------
def listar(aluno):
    print('\n--- Listagem Alunos ---')

    for i in aluno:
        print( 'Id: ' + str(i['id']) + '\n' +
               'Cpf: ' + i['cpf'] + '\n' +
               'Nome: ' + i['nome'] + '\n' +
               'Idade: ' + str(i['idade']) + '\n' +
               'Turma: ' + i['turma'] + '\n' +
               '-----------------------' )

    opcao = int(input('\nDeseja atualizar algum aluno? [1-Sim/2-Não]: '))
    if opcao == 1:
        print('\n--- Atualizar Aluno ---')
        print('1 - Editar')
        print('2 - Deletar')
        print('3 - Menu')
        print('-----------------------\n')

        opcao = int(input('Informe a Opção: '))
        if opcao == 1:
            editar(aluno)

        elif opcao == 2:
            deletar(aluno)

        elif opcao == 3:
            opcoes(aluno)

        else:
            print('\nOpção inválida!')
            return opcoes(aluno)

    else:
        opcao = int(input('\nDeseja retornar ao menu? [1-Sim/2-Não]: '))
        if opcao == 1:
            opcoes(aluno)

        else:
            exit()

    # --------FUNÇÃO PARA EDITAR ALUNO-------


def editar(aluno):
    print('\n--- Editar Aluno ---')

    id = int(input("Digite o código: "))
    for i, key in enumerate(aluno):
        if (id == key["id"]):
            key['cpf'] = input('Cpf: ')
            key['nome'] = input('Nome: ')
            key['idade'] = int(input('Idade: '))
            key['turma'] = input('Turma: ')

            print('--------------------\n')
            print('Dados atualizados!')

    opcao = int(input('\nDeseja retornar ao menu? [1-Sim/2-Não]: '))
    if opcao == 1:
        opcoes(aluno)

    else:
        exit()

    # -------FUNÇÃO PARA DELETAR ALUNO------


def deletar(aluno):
    id = int(input("\nDigite o código: "))
    for i, key in enumerate(aluno):
        if (id == key["id"]):
            del aluno[i]
            print('Aluno deletado!')

    opcao = int(input('\nDeseja retornar ao menu? [1-Sim/2-Não]: '))
    if opcao == 1:
        opcoes(aluno)

    else:
        exit()

    # -------FUNÇÃO PARA FECHAR O CÓDIGO------
def sair(lista):
    opcao = int(input('\nTem certeza que quer sair? [1-Sim/2-Não]: '))
    if opcao == 1:
        print('******Você saiu!******')
        exit()

    else:
        opcoes(lista)



if __name__ == '__main__':
    opcoes(aluno)