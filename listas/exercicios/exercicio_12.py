def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)
    media = total / quantidade
    print(f'A média das notas é: {media}')
notas = []

while True:
    nota = float(input('Digite uma nota ou 0 para parar: '))
    if nota == 0:
        break
    else:
        notas.append(nota)

calcular_media(notas)