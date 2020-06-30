def validacao_CPF(cpf):
    cpf = str(cpf)
    if len(cpf) != 11:
        return False
    cpf_9digitos = cpf[:9]
    # variáveis para os loops dos laços e para somas
    loop1 = 10
    loop2 = 11
    soma1 = soma2 = 0
    # gerando dígito 1
    for i in cpf_9digitos:
        soma1 += int(i) * loop1
        loop1 -= 1
    result1 = 11 - (soma1 % 11)
    digito1 = result1 if result1 <= 9 else 0

    cpf_verificado = cpf_9digitos + str(digito1)
    # gerando dígito 2
    for j in cpf_verificado:
        soma2 += int(j) * loop2
        loop2 -= 1
    result2 = 11 - (soma2 % 11)
    digito2 = result2 if result2 <= 9 else 0

    cpf_verificado += str(digito2)

    return True if str(cpf) == str(cpf_verificado) else False


def gerar_CPF():
    from random import randint
    cpf = ''
    for n in range(0, 9):                               # gerando nove primeiros números
        n = str(randint(0, 9))
        cpf += n
    loop1 = 10
    loop2 = 11
    soma1 = soma2 = 0
    for i in cpf:                                       # gerando dígito 1
        soma1 += int(i) * loop1
        loop1 -= 1
    d1 = 11 - (soma1 % 11)
    digito1 = d1 if d1 <= 9 else 0

    cpf += str(digito1)

    for j in cpf:                                       # gerando dígito 2
        soma2 += int(j) * loop2
        loop2 -= 1
    d2 = 11 - (soma2 % 11)
    digito2 = d2 if d2 <= 9 else 0

    cpf += str(digito2)

    return cpf

