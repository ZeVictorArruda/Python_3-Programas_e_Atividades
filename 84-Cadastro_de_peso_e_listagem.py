'''Programa para cadastro de nome e peso, mostrando, ao final, quantas pessoas
foram cadatraadas, o maior peso e o menor e quem pesava mais e menos'''
# O programa será realizado utilizando duas listas:
# A lista temp receberá os dados temporariamente.
# Os dados serão inseridos definifitamente na lista geral, onde serão armazenados
geral = []
temp = []
pesado = leve = 0
while True:
    temp.append(str(input('Nome: ')).strip())
    temp.append(float(input('Peso: ')))
    if len(geral) == 0:
        pesado = leve = temp[1]
    else:
        if temp[1] > pesado:
            pesado = temp[1]
        if temp[1] < leve:
            leve = temp[1]
    geral.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar? (S/N): ')).lower().strip()
    while resp not in 'sn':
        resp = str(input('Comando inválido. Digite S para sim e N para não. Desaja continuar? '))
    if resp == 'n':
        break
print('-' * 30)
print(f'Pessoas cadastradas: {len(geral)}')
print(f'O maior peso cadastrado foi: {pesado}kg. Em:')
for p in geral:
    if p[1] == pesado:
        print(p[0])
print(f'O menor peso cadastrado foi: {leve}kg. Em:')
for l in geral:
    if l[1] == leve:
        print(l[0])