def numero():
    numero = int(input('Digite um número inteiro: '))

    if numero > 0:
        tipo = 'positivo'
    elif numero < 0:
        tipo = 'negativo'
    else:
        tipo = 'zero'

    if numero % 2 == 0:
        classificacao = 'par'
    else:
        classificacao = 'ímpar'

    print(f'Número: {numero}')
    print(f'Classificação: {tipo} e {classificacao}')

numero()