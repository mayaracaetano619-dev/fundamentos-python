def combustivel():
    distancia = int(input('Digite a distância percorrida em km: '))
    combustivel = int(input('Digite a quantidade de combustível em litros: '))

    consumo = distancia / combustivel

    print(f'O consumo médio é: {consumo:} km/L')


combustivel()