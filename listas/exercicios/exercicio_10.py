def inverter_lista(lista):
    nova_lista = list(reversed(lista))
    print(f'Lista invertida: {nova_lista}')
lista = []

while True:
    item = input('Digite um item ou 0 para parar: ')
    if item == '0':
        break
    else:
        lista.append(item)

inverter_lista(lista)