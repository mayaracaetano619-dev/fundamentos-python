def adicionar_produtos(compras, produtos):
    compras.extend(produtos)
compras = ['Arroz', 'Feijão', 'Leite']
produtos = []
while True:
    produto = input('Digite um produto ou 0 para parar: ')
    if produto == '0':
        break
    produtos.append(produto)


adicionar_produtos(compras, produtos)

def cancelar_compra(compras, produto):
    compras.remove(produto)
produto = input('Digite o produto que deseja cancelar: ')

cancelar_compra(compras, produto)
print(f'Lista de compras: {compras}')