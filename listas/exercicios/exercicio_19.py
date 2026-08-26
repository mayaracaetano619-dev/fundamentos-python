def adicionar_nota(notas, nota):
    notas.append(nota)

def inserir_nota(notas, nota, posicao):
    notas.insert(posicao, nota)

def adicionar_varias(notas, novas_notas):
    notas.extend(novas_notas)

def remover_nota(notas, nota):
    notas.remove(nota)

def remover_ultima(notas):
    notas.pop()

def encontrar_nota(notas, nota):
    posicao = notas.index(nota)
    print(f'A nota está na posição: {posicao}')

def quantidade_notas(notas):
    quantidade = len(notas)
    print(f'A quantidade de notas é: {quantidade}')
notas = [7.5, 6.0, 8.5, 9.0, 5.5]
nota = float(input('Digite uma nova nota: '))


adicionar_nota(notas, nota)
nota = float(input('Digite uma nota para inserir: '))
posicao = int(input('Digite a posição: '))


inserir_nota(notas, nota, posicao)
novas_notas = []
while True:
    nota = float(input('Digite uma nota ou 0 para parar: '))
    if nota == 0:
        break
    novas_notas.append(nota)

adicionar_varias(notas, novas_notas)
nota = float(input('Digite a nota que deseja remover: '))
remover_nota(notas, nota)


remover_ultima(notas)
nota = float(input('Digite a nota que deseja encontrar: '))


encontrar_nota(notas, nota)


quantidade_notas(notas)
print(f'Lista final de notas: {notas}')