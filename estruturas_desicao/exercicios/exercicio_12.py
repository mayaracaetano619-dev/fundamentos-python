def login():
    print('-----LOGIN-----')
    senha = input('Digite a senha: ')

    if senha == 'python123':
        print('Acesso permitido')
    else:
        print('Senha inválida')

login()