def prestacao():
    valor_produto = float(input('Digite o valor do produto: R$ '))
    parcelas = int(input('Digite a quantidade de parcelas: '))

    valor_parcela = valor_produto / parcelas

    print(f'O valor de cada parcela é: R$ {valor_parcela}')


prestacao()