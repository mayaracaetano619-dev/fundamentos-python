def remover_produto(produtos, produto):
    while produto not in produtos:
        print('Produto não encontrado!')
        produto = input('Digite outro produto: ')

    produtos.remove(produto)
    print(f'Lista de produtos: {produtos}')


produtos = ['Arroz', 'Feijão', 'Macarrão', 'Leite', 'Café']

produto = input('Digite o produto que deseja remover: ')

remover_produto(produtos, produto)