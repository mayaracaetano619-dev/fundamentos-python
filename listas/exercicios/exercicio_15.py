def adicionar_nota(notas, nota):
    notas.append(nota)

def remover_nota(notas, nota):
    notas.remove(nota)

def media_notas(notas):
    media = sum(notas) / len(notas)
    print(f'A média das notas é: {media}')
notas = []
while True:
    nota = float(input('Digite uma nota ou 0 para parar: '))
    if nota == 0:
        break
    adicionar_nota(notas, nota)
nota = float(input('Digite a nota que deseja remover: '))
remover_nota(notas, nota)
media_notas(notas)