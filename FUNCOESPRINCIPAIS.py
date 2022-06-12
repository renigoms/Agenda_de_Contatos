# --------------------------------------------------------------------------------------
# CADASTRO DE CONTATOS:
# --------------------------------------------------------------------------------------
salvar = []
lista = []


def cadastrarcontato():
    # variaveis;
    listinfo = []
    opcao = None
    # adição de informações;
    while True:
        print('-' * 35)
        print('|       CADSTRAR NOVO CONTATO     |')
        print('-' * 35)
        email = (input('|E-MAIL DO CONTATO: '))
        if checaremail(email):
            print('ESTE E-MAIL JÁ EXISTE. LOGO ESSE CONTATO TAMBÉM.')
            return cadastrarcontato()
        print('-' * 35)
        nome = input('|NOME DO CONTATO:')
        print('-' * 35)
        sobrenome = input('|SOBRENOME DO CONTATO: ')
        print('-' * 35)
        apelido = input('|APELIDO DO CONTATO:')
        print('-' * 35)
        while True:
            numero = input('|NUMERO(s)) DO CONTATO:')

            lista.append(numero)
            op = input('QUER ADICIONAR MAIS UM NÚMERO?:[S/N]').upper()
            if op == 'N':
                break
        print('-' * 35)
        endereco = input('|ENDEREÇO DO CONTATO:')
        # agrupamento de informações;
        listinfo = [email, nome, sobrenome, apelido, lista[:], endereco]
        lista.clear()
        salvar.append(listinfo)
        print('-' * 35)
        # opcao de cadastrar outro contato ou não;
        opcao = int(input('QUER CADASTRAR MAIS UM CONTATO? [1]-SIM E [2]-NÃO: '))
        if opcao != 1:
            print('CONTATO SALVO COM SUCESSO')
            print('-' * 35)
            break
        print('-' * 35)


# ============================================================================================
# LISTAGEM DE CONTATOS
# ============================================================================================
def listarcontatos():
    r = range(0, len(salvar))
    print('*' * 15, 'LISTA DE CONTATOS', '*' * 15)

    for i in r:
        print('+*+' * 15)
        print(f'{i + 1}° CONTATO')
        print('+*+' * 15)
        print(f'E-MAIL DO CONTATO: {salvar[i][0]} ', end='')
        print(f'/ NOME DO CONTATO: {salvar[i][1]} ', )
        print(f'SOBRENOME DO CONTATO: {salvar[i][2]} ', end='')
        print(f'/ APELIDO DO CONTATO: {salvar[i][3]} ')
        print(f'NÚMERO DO CONTATO: {salvar[i][4]} ', end='')
        print(f'/ ENDEREÇO DO CONTATO:{salvar[i][5]} ')
        print('+*+' * 15)


# ==============================================================================================
# VERIFICAR DE A INFORMAÇÃO ESTÁ REPETIDO/VERIFICAÇÃO DE CONTATO REPETIDO
# ==============================================================================================
def checaremail(email):
    cadastrado = False
    for i in range(0, len(salvar)):
        if email == salvar[i][0]:
            cadastrado = True
    return cadastrado


# =============================================================================================
# EDITAR CONTATOS
# ============================================================================================
def editcontato():
    conteditavel = []
    editar = input('QUAL O E-MAIL DO CONTATO QUE VOCÊ QUER EDITAR?')
    if checaremail(editar):
        for i, conteditavel in enumerate(salvar):
            if conteditavel[0] == editar:
                print(editar)
                opcao = input(f'DESEJA EDITAR O CONTATO {conteditavel[1], conteditavel[2]}? [S/N]').upper()
                if opcao == 'S':
                    op1 = input(f'DESEJA EDITAR O E-MAIL? [S/N]').upper()
                    if op1 == 'S':
                        print('-' * 35)
                        email = (input('|E-MAIL DO CONTATO: '))
                        conteditavel[0] = email
                        print('-' * 35)
                    op2 = input(f'DESEJA EDITAR O NOME? [S/N]').upper()
                    if op2 == 'S':
                        print('-' * 35)
                        nome = input('|NOME DO CONTATO:')
                        conteditavel[1] = nome
                        print('-' * 35)
                    op3 = input(f'DESEJA EDITAR O SOBRENOME? [S/N]').upper()
                    if op3 == 'S':
                        print('-' * 35)
                        sobrenome = input('|SOBRENOME DO CONTATO: ')
                        conteditavel[2] = sobrenome
                        print('-' * 35)
                    op4 = input(f'DESEJA EDITAR O APELIDO? [S/N]').upper()
                    if op4 == 'S':
                        print('-' * 35)
                        apelido = input('|APELIDO DO CONTATO:')
                        conteditavel[3] = apelido
                        print('-' * 35)
                    op5 = input(f'DESEJA EDITAR O(S) NÚMEROS? [S/N]').upper()
                    if op5 == 'S':
                        print('-' * 35)
                        while True:
                            numero = input('|NUMERO(s)) DO CONTATO:')
                            lista.append(numero)
                            op = input('QUER ADD MAIS UM?:[S/N]').upper()
                            if op == 'N':
                                break
                        conteditavel[4] = lista
                        print('-' * 35)
                    op6 = input(f'DESEJA EDITAR O ENDEREÇO? [S/N]').upper()
                    if op6 == 'S':
                        print('-' * 35)
                        endereco = input('|ENDEREÇO DO CONTATO:')
                        conteditavel[5] = endereco
                        print('-' * 35)
                    salvar[i] = conteditavel
                    print(conteditavel)
                    print('CONTATO EDITADO COM ÊXITO.')
    else:
        print('CONTATO NÃO ENCONTRADO')
        op = input('QUER VOLTAR AO MENU?[S/N]:').upper()
        if op == 'S':
            print('RETORNANDO AO MENU.')
        else:
            return editcontato()


# =============================================================================================
# REMOVER CONTATO
# ============================================================================================
def removercontato():
    contato = []
    delete = input('QUAL O E-MAIL DO CONTATO QUE VOCÊ QUER REMOVER?: ')
    if checaremail(delete):
        for i, contato in enumerate(salvar):
            if contato[0] == delete:
                print(delete)
                opcao = int(input(f'REALMENTE DESEJA REMOVER O CONTATO {contato[1]} {contato[2]} DA SUA LISTA'
                                  f' DE CONTATOS? [1]-SIM E [2]-NÃO: '))
                if opcao == 1:
                    salvar.pop(i)
                    print('CONTATO REMOVIDO!!!')
    else:
        print('ESTE CONTATO NÃO ESTÁ CADSTRADO.')
        op = input('QUER VOLTAR AO MENU?[S/N]: ').upper()
        if op == 'S':
            print('RETORNANDO AO MENU.')
        else:
            return removercontato()
