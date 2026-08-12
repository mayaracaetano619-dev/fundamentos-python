def imc():
    peso = float(input('Digite seu peso em kg: '))
    altura = float(input('Digite sua altura em metros: '))

    imc = peso / (altura * altura)

    print(f'IMC: {imc}')

    if imc < 18.5:
        print('Abaixo do peso')
    elif imc <= 24.9:
        print('Peso normal')
    elif imc <= 29.9:
        print('Sobrepeso')
    else:
        print('Obesidade')


imc()