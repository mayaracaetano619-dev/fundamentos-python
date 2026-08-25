def eh_primo():
    numero = int(input("Digite um número: "))

    if numero < 2:
        print(f"{numero} não é primo")
        return

    for i in range(2, numero):
        if numero % i == 0:
            print(f"{numero} não é primo")
            return

    print(f"{numero} é primo")


eh_primo()