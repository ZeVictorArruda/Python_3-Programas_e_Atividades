# Funções de interface:

def lerint(numero):
    while True:
        try:
            n = int(input(numero))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite uma opção válida')
        else:
            return n


def cabecalho(txt):
    print('-' * 40)
    print(txt.center(40))
    print('-' * 40)


def menu(lista):
    cabecalho('Menu principal')
    c = 1
    for i in lista:
        print(f'{c} - {i}')
        c += 1
    print('-' * 40)
    opc = lerint('Digite sua opção: ')
    return opc
