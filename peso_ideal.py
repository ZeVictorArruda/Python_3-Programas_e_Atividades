#cálculo de peso ideal através de IMC
altura = float(input('Insira sua altura: '))
peso = float(input('Insira seu peso: '))
imc = peso / (altura ** 2)
if 18.5 < imc <= 24.9:
    print('Você está dentro do peso ideal.')
else:
    peso_minimo = 18.6 * (altura ** 2)
    peso_maximo = 24.9 * (altura ** 2)
    if imc <= 18.5:
        print('Você está abaixo do peso ideal.')
    elif 25 <= imc <= 29.9:
        print('Você está acima do peso.')
    elif 30 <= imc <= 34.9:
        print('Você está com obesidade grau 1')
    elif 35 <= imc <= 39.9:
        print('Você está com obesidade grau 2')
    else:
        print('Você está com obesidde grau 3')
    print(f'Seu peso ideal se encontra entre {round(peso_minimo, 2)}kg e {round(peso_maximo, 2)}kg')
