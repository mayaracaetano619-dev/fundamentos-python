def encontrar_produto(produtos, produto):
    posicao = produtos.index(produto)
    print(f'O produto está na posição: {posicao}')

produto = input('Digite o produto que deseja encontrar: ')
produtos = ['Arroz', 'Feijão', 'Macarrão', 'Leite', 'Café']


encontrar_produto(produtos, produto)