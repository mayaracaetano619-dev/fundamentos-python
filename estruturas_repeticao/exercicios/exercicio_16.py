def validar_senha():
    senha_correta = "1234"
    tentativas = 0

    while tentativas < 3:
        senha = input("Digite a senha: ")

        if senha == senha_correta:
            print("Acesso permitido!")
            return

        print("Senha incorreta!")
        tentativas += 1

    print("Acesso bloqueado!")


validar_senha()