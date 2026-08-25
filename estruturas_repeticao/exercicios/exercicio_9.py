def contar_pares():
    inicio = int(input('Digite o início: '))
    fim = int(input('Digite o fim: '))
    quantidade = 0

    for numero in range(inicio, fim + 1):
        if numero % 2 == 0:
            quantidade += 1

    return quantidade

resultado = contar_pares()

print(f'Quantidade de números pares:{resultado}')