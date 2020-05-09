#cálculo de peso ideal através de IMC utilizando listas e dicionários para armazenar os dados
pessoa = {}
lista = []

while True:
    pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
    pessoa['altura'] = float(input('Altura: '))
    pessoa['peso'] = float(input('Peso: '))
    imc = round(pessoa['peso'] / (pessoa['altura'] ** 2), 2)
    pessoa['imc'] = imc
    if 18.5 >= imc:
        pessoa['situação'] = 'Abaixo do peso ideal'
    elif 18.5 < imc <= 24.9:
        pessoa['situação'] = 'Peso ideal'
    elif 25 <= imc <= 29.9:
        pessoa['situação'] = 'Acima do peso'
    elif 30 <= imc <= 34.9:
        pessoa['situação'] = 'Obesidade grau 1'
    elif 35 <= imc <= 39.9:
        pessoa['situação'] = 'Obesidade grau 2'
    else:
        pessoa['situação'] = 'Obesidade grau 3'
    lista.append(pessoa.copy())
    pessoa.clear()
    resp = str(input('Continuar cadastro? (S/N): ')).lower().strip()
    while resp not in 'sn':
        resp = str(input('Comando inválido. Deseja continuar o cadastro? (Digite S para sim ou N para não) '))
    if resp == 'n':
        break

print('-' * 30)
print(f'{"|No":<3} {"|NOME":<15} {"|ALTURA":<15} {"|PESO":<15} {"|IMC":<15} {"|SITUAÇÃO":<20}')
for i, c in enumerate(lista):
    print(f'|{i+1:<3}', end='')
    for k, v in c.items():
        print(f'|{v:<15}', end='')
    print()
