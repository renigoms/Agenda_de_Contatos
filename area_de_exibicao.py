from FUNCOESPRINCIPAIS import*
from MENU import*
def main():
    op = None
    while True:
        op = menu()
        if op == 1:
            cadastrarcontato()
        elif op == 2:
            listarcontatos()
        elif op == 3:
            editcontato()
        elif op == 4:
            removercontato()
        elif op == 5:
            print('programa encerrado!!')
            break
        else:
            print('ESSE NÃO É UM VALOR VÁLIDO')
            return main()
main()
