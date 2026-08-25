def somar_pares():
    inicio = int(input("Digite o início: "))
    fim = int(input("Digite o fim: "))

    soma = 0

    for numero in range(inicio, fim + 1):
        if numero % 2 == 0:
            soma = soma + numero

    print(f"Soma dos números pares: {soma}")


somar_pares()