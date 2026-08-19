def mostrar_numero_while():
    contador = 0
    while contador <= 10:
        contador += 1
        print(f'Contagem atual: {contador}')

# mostrar_numero_while()

def contagem_regressiva():
    valor_contagem = int(input('Digite um nímero maior que 10: '))
    if valor_contagem < 10:
        print('Valor inválido')
    else:
        while valor_contagem >= 1:
            print(f'Contagem regressiva: {valor_contagem}')
            valor_contagem -= 1
        print('Decolando!!')

# contagem_regressiva()

def soma_finita():
    while True:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))

        if num1 == 0:
            break
        else:
            soma = num1 + num2
            print(f'O resultado da soma é {soma}')

soma_finita()