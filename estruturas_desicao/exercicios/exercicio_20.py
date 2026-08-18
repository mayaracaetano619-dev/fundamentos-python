def banco():
    saldo = float(input('Digite o saldo disponível: R$ '))
    saque = float(input('Digite o valor que deseja sacar: R$ '))

    if saque <= 0:
        print('Valor de saque inválido')
    elif saque > saldo:
        print('Saldo insuficiente')
    else:
        novo_saldo = saldo - saque
        print('Saque realizado com sucesso!')
        print(f'Novo saldo: R$ {novo_saldo}')


banco()