def frete():
    valor_compra = float(input('Digite o valor da compra: R$ '))

    if valor_compra <= 100:
        frete = 20
    elif valor_compra <= 300:
        frete = 10
    else:
        frete = 0

    valor_total = valor_compra + frete

    print(f'Valor da compra: R$ {valor_compra}')
    print(f'Valor do frete: R$ {frete}')
    print(f'Valor total: R$ {valor_total}')


frete()