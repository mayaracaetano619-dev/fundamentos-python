def conta_energia():
    consumo = float(input('Digite o consumo em kWh: '))
    preco_kwh = float(input('Digite o preço do kWh: R$ '))

    valor_conta = consumo * preco_kwh

    print(f'O valor da conta de energia é: R$ {valor_conta}')


conta_energia()