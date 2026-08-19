# Laço for simples
import time

def mostar_numero():
    for i in range (1, 6):
        print(f"O número atual é: {i}")
        time.sleep(1)

# mostar_numero()

def mostar_numero_alternado():
    for num in range(0, 20, 2):
        print(f"O número atual é {num}")
        time.sleep(1)

# mostar_numero_alternado()

def somar_numeros():
    total = 0
    for valor in range(1, 20):
        total += valor

    print(total)

# somar_numeros()

def mostar_numeros_pares():
    for numero in range(1, 21):
        if numero % 2 == 0:
            print(f'Números pares: {numero}')

# mostar_numeros_pares()


def mostrar_item_da_lista():
    sacola_de_frutas = ['Maçã', 'Banana', 'Pera', 'Abacate']
    for fruta in sacola_de_frutas:
        print(f'Na minha sacola contém {fruta}')

# mostrar_item_da_lista()


def laco_alinhado():
    nomes = ['Mayara', 'Sophia', 'Mariana']
    notas = [8, 9, 10]
    for nome in nomes:
        print(f'Nome do aluno: {nome}')
        for nota in notas:
            print(f'Nota do aluno: {nota}')

# laco_alinhado()