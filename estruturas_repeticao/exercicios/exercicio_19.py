def menu():
    opcao = 0

    while opcao != 4:
        print("--- MENU ---")
        print("1 - Exibir números de 1 a 10")
        print("2 - Exibir números pares")
        print("3 - Exibir tabuada")
        print("4 - Sair")

        opcao = int(input("Digite uma opção: "))

        if opcao == 1:
            for numero in range(1, 11):
                print(f"{numero}")

        elif opcao == 2:
            for numero in range(2, 11, 2):
                print(f"{numero}")

        elif opcao == 3:
            numero = int(input("Digite um número: "))
            for i in range(1, 11):
                print(f"{numero} x {i} = {numero * i}")

        elif opcao == 4:
            print("Programa encerrado!")

        else:
            print(f"A opção {opcao} é inválida!")


menu()