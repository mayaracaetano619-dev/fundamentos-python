def contagem_regressiva():
    valor_contagem = int(input('Digite um nímero: '))
    while valor_contagem >= 0:
            print(f'Contagem regressiva: {valor_contagem}')
            valor_contagem -= 1

contagem_regressiva()