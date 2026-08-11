def aluno_aprovado():
    nota_1 = float(input('Digite sua primeira nota: '))
    nota_2 = float(input('Digite sua segunda nota: '))

    media = (nota_1 + nota_2) / 2

    if media >= 9:
        print('Aluno aprovado!')
    elif media >= 5 and media < 6:
        print('Aluno de Recuperação!')
    else:
            print('Aluno reprovado!')

# aluno_aprovado()







def login():
    e_mail = "mayaracaetano619@gmail.com"
    senha = "1234"
    codigo_segreto = "#5678"

    email_input = input('Digite o seu e-mail: ')
    senha_input = input('Digite sua senha: ')

    if email_input == e_mail and senha_input == senha:
        print('Usuário logado!')
        acessar_admin = input('Deseja acessar área administrativa? [S/N]')
        if acessar_admin == 'S':
            codigo_segreto_input = input('Digite o seu codigo secreto: ')
            if codigo_segreto_input == codigo_segreto:
                print('Acesso adm liberado!')
            else:
                print('Código secreto incorreto!')
        elif acessar_admin == 'N':
            print('Ok. Você acessou como usuário comum')
        else:
            print('Opção invalida!')
    else:
        print('E-mail ou senha incorreta!')

login()