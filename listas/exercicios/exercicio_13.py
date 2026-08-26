def adicionar_cliente(fila, cliente):
    fila.append(cliente)
fila = []
while True:
    cliente = input('Digite o nome do cliente ou 0 para parar: ')

    if cliente == '0':
        break

    adicionar_cliente(fila, cliente)
def atender_cliente(fila):
    cliente = fila.pop(0)
    return cliente
cliente_atendido = atender_cliente(fila)

print(f'Cliente atendido: {cliente_atendido}')
print(f'Fila restante: {fila}')