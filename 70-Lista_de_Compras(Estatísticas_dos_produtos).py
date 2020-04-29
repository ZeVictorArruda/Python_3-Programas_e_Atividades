"""O programa abaixo irá ler o nome e o preço de um produto. Ao final, o programa mostrará:
- Total de produtos inseridos
- Valor total dos produtos
- Quantos produtos custam mais de mil reais
- Nome e valor do produto mais barato
- Nome e valor do produto mais caro"""

barato = caro = ''
total = menor = maior = cont = maior_mil = 0
while True:
    produto = str(input('Produto: '))  # Usuário insere o nome do produto
    valor = float(input('Valor: R$ '))  # Usuário insere valor do produto
    total += valor
    cont += 1
    if cont == 1:
        menor = valor
        barato = produto
        maior = valor
        caro = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto
        elif valor > maior:
            maior = valor
            caro = produto
    if valor > 1000:
        maior_mil += 1
    resp = str(input('Desaja continuar? (S/N): ')).lower().strip()
    while resp not in 'sn':
        resp = str(input('Insira S para sim e N para não. Desaja continuar? ')).lower().strip()
    if resp == 'n':
        break
print('-' * 10, 'Resumo dos produtos:', '-' * 10)
print(f'Total de produtos: {cont}\nValor total da lista: {total:.2f}\nProdutos que custam mais mil reais: {maior_mil}')
print(f'Produto mais caro: {caro}\nValor do produto mais caro: R$ {maior}')
print(f'Produto mais barato: {barato}\nValor do produto mais barato: R$ {menor}')
