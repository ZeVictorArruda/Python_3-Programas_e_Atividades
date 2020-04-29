"""O programa abaixo irá ler o nome e o preço de um produto. Ao final, o programa mostrará:
- Total de produtos inseridos
- Valor total dos produtos
- Quantos produtos custam mais de mil reais
- Nome e valor do produto mais barato
- Nome e valor do produto mais caro"""
barato = caro = ''
total = valor_barato = valor_caro = cont = maior_mil = 0
while True:
    produto = str(input('Produto: ')) #Aqui o usuário insere o nome do produto