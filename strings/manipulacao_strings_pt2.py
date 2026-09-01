# dividir uma string em partes
def separar_nome(nome_completo):
    partes = nome_completo.split()
    return partes

nome_completo = input('Digite Seu nome completo: ')
print(f'Nome em partes: {separar_nome(nome_completo)}')

#Juntar Strings
def criar_nome_completo(partes):
    nome_completo = ' '.join(partes)
    return nome_completo

partes_nome = ['Mayara', 'Caetano']
print(f'Nome completo: {criar_nome_completo(partes_nome)}')