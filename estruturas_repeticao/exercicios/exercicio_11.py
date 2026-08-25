def fatorial():
    numero = int(input('Digite um número: '))

    resultado = 1

    for i in range(1, numero + 1):
        resultado *= i

    return resultado

resultado = fatorial()

print(f'Fatorial:{resultado}')