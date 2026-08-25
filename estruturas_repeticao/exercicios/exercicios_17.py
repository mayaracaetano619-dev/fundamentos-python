def jogo_adivinhacao(numero_secreto):
    acertou = False

    while acertou == False:
        numero = int(input("Digite um número: "))

        if numero == numero_secreto:
            print("Você acertou!")
            acertou = True

        elif numero < numero_secreto:
            print(f"O número secreto é maior que {numero}!")

        else:
            print(f"O número secreto é menor que {numero}!")


numero_secreto = 10

jogo_adivinhacao(numero_secreto)