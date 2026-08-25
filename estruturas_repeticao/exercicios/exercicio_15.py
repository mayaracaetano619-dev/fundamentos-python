def maior_numero():
    maior = float(input("Digite um número: "))
    continuar = "s"

    while continuar == "s":
        numero = float(input("Digite outro número: "))

        if numero > maior:
            maior = numero

        continuar = input("Deseja continuar? (s/n): ")

    print(f"O maior número foi: {maior}")


maior_numero()