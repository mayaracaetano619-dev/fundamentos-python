def adicionar_nome(nomes):
    while True:
        nome = input('Digite um nome ou (n) para parar: ')

        if nome == 'n':
            break
        else:
            nomes.append(nome)

    print(f'Nomes: {nomes}')


nome = []
adicionar_nome(nome)