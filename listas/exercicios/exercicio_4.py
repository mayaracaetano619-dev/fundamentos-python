def remover_produto(produtos, produto):
    produtos.remove(produto)
    print(f'Lista de produtos: {produtos}')

produto = input('Digite o produto que deseja remover: ')
produtos = ['Arroz', 'Feijão', 'Macarrão', 'Leite', 'Café']


remover_produto(produtos, produto)