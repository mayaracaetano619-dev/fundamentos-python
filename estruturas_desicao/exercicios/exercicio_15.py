def radar():
    velocidade = int(input('Digite a velocidade do veículo em km/h: '))

    if velocidade <= 60:
        print('Velocidade permitida')
    elif velocidade <= 80:
        print('Atenção: velocidade acima do permitido')
    else:
        print('Multa por excesso de velocidade')


radar()