def desconto():
    preco = int(input('Digite o preço do produto: R$ '))
    percentual = int(input('Digite o percentual de desconto: '))

    desconto = percentual / 100
    valor_desconto = preco * desconto
    valor_final = preco - valor_desconto

    print(f"Valor do desconto: R$ {valor_desconto:}")
    print(f"Valor final: R$ {valor_final: }")


desconto()