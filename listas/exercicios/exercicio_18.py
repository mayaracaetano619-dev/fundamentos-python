def analisar_temperaturas(temperaturas):
    quantidade = len(temperaturas)
    soma = sum(temperaturas)
    media = soma / quantidade
    ordenadas = sorted(temperaturas)
    return quantidade, soma, media, ordenadas
temperaturas = []
while True:
    temperatura = float(input('Digite uma temperatura ou 0 para parar: '))
    if temperatura == 0:
        break
    temperaturas.append(temperatura)

quantidade, soma, media, ordenadas = analisar_temperaturas(temperaturas)
print(f'Quantidade de temperaturas: {quantidade}')
print(f'Soma das temperaturas: {soma}')
print(f'Média das temperaturas: {media}')
print(f'Temperaturas ordenadas: {ordenadas}')