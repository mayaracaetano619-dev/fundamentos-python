def mostrar_primos():
    inicio = int(input('Digite o início: '))
    fim = int(input('Digite o fim: '))
    for numero in range(inicio, fim + 1):
        if numero >= 2:
            primo = True

            for i in range(2, numero):
                if numero % i == 0:
                    primo = False
                    break

            if primo:
                print(numero)

mostrar_primos()