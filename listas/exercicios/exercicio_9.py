def ordenar_nomes(nomes):
    nova_lista = sorted(nomes)
    print(f'Nomes em ordem alfabética: {nova_lista}')
nomes = []

while True:
    nome = input('Digite um nome ou 0 para parar: ')
    if nome == '0':
        break
    else:
        nomes.append(nome)

ordenar_nomes(nomes)