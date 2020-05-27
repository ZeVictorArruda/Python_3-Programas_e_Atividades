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

print(f'{"|No":<3} {"|NOME":<15} {"|SITUAÇÃO":<20}')
for i, j in enumerate(lista):
    print(f'|{i+1:<3}|{j["nome"]:<15}|{j["situação"]:<20}')

print('-' * 30)

print('Caso deseje ver os dados de alguém, digite o número no espaço abaixo (Digite 0 para encerrar):')

while True:
    n = int(input('Deseja ver os dados de alguém? '))
    if n == 0:
        break
    if n <= len(lista):
        print(f'Mostrando dados de: {lista[n-1]["nome"]}')
        print(f'Altura: {lista[n-1]["altura"]:.2f}m\nPeso: {lista[n-1]["peso"]}kg\nIMC: {lista[n-1]["imc"]}')

print('-' * 30, '\nEncerrado')
