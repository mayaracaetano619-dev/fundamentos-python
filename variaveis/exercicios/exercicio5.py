DESCONTO_MAXIMO = 0.10
preco_produto = 1350
desconto = preco_produto * DESCONTO_MAXIMO
preco_final = preco_produto - desconto

print(f'O total da compra foi R${preco_final}')
