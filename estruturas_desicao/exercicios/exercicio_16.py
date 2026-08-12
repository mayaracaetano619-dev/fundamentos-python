def realizar_login():
    usuario = input('Digite o usuário: ')
    senha = input('Digite a senha: ')

    if senha == '1234':
        print('Usuário incorreto')
    elif usuario == 'admin':
        print('Senha incorreta')
    else:
        print('Login realizado com sucesso')


realizar_login()