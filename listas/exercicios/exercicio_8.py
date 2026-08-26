def ordenar_numeros(numeros):
    nova_lista = sorted(numeros)
    print(f'Números em ordem crescente: {nova_lista}')
numeros = []

while True:
    numero = int(input('Digite um número ou 0 para parar: '))
    if numero == 0:
        break
    else:
        numeros.append(numero)

ordenar_numeros(numeros)