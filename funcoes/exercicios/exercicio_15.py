def idade():
    idade = int(input('Qual a sua idade? '))

    meses = idade * 12
    dias = idade * 365

    print(f'Você tem {meses} meses de idade.')
    print(f'Você tem {dias} dias de idade.')


idade()