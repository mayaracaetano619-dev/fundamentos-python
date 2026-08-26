def adicionar_convidados(convidados, novos_convidados):
    convidados.extend(novos_convidados)
    print(f'Lista de convidados: {convidados}')

convidados = ['Mayara', 'Sophia', 'Nicolas']
novos_convidados = []

while True:
    nome = input('Digite o nome do novo convidado ou 0 para parar: ')

    if nome == '0':
        break
    else:
        novos_convidados.append(nome)

adicionar_convidados(convidados, novos_convidados)