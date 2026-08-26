def somar_numeros(numeros):
    soma = sum(numeros)
    print(f'A soma dos números é: {soma}')
numeros = []

while True:
    numero = int(input('Digite um número ou 0 para parar: '))
    if numero == 0:
        break
    else:
        numeros.append(numero)

somar_numeros(numeros)