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


def arqexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close
    except:
        print('Erro ao criar arquiv.')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        for linha in a:
            cabecalho('PESSOAS CADASTRADAS')
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()
