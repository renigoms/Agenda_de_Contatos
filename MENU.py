#---------------------------------------------------------------------------------------------
#MENU:
#---------------------------------------------------------------------------------------------
def menu():
    print('+-'*25)
    print('|                AGENDA DE CONTATOS              |')
    print('+-'*25)
    print("""         
             [1]-CADASTRO:
             [2]-LISTA DE CONTATOS
             [3]-EDITAR CONTATOS
             [4]-REMOVER CONTATO
             [5]-SAIR
             """)
    print('+-'*25)
    opcao = int(input('ESCOLHA UMA DAS OPÇÕES:'))
    print('+-'*25)
    return opcao