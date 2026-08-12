def ingresso():
    idade = int(input('Digite a idade: '))

    if idade <= 5:
        print('Ingresso gratuito')
    elif idade <= 12:
        print('Preço do ingresso: R$ 10,00')
    elif idade <= 59:
        print('Preço do ingresso: R$ 20,00')
    else:
        print('Preço do ingresso: R$ 10,00')

ingresso()