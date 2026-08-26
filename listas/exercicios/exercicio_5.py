def remover_item(itens, posicao):
    item_removido = itens.pop(posicao)
    return item_removido

posicao = int(input('Digite a posição do item que deseja remover: '))
itens = ['Arroz', 'Feijão', 'Macarrão', 'Leite', 'Café']

resultado = remover_item(itens, posicao)
print(f'Item removido: {resultado}')
print(f'Lista de itens: {itens}')