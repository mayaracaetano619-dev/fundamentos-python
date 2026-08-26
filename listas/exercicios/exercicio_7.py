def quantidade_elementos(lista):
    quantidade = len(lista)
    print(f'A quantidade de frutas é: {quantidade}')
frutas = []

while True:
    fruta = input('Digite uma fruta ou 0 para parar: ')
    if fruta == '0':
        break
    else:
        frutas.append(fruta)

quantidade_elementos(frutas)