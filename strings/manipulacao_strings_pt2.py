# dividir uma string em partes
def separar_nome(nome_completo):
    partes = nome_completo.split()
    return partes

#nome_completo = input('Digite Seu nome completo: ')
#print(f'Nome em partes: {separar_nome(nome_completo)}')

#Juntar Strings
def criar_nome_completo(partes):
    nome_completo = ' '.join(partes)
    return nome_completo

partes_nome = ['Mayara', 'Caetano']
#print(f'Nome completo: {criar_nome_completo(partes_nome)}')

# Verificar o início e o final de uma string
def analizar_url(url):
    com_https = url.startswith('https://')
    termina_com_br = url.endswith('.br')
    return com_https, termina_com_br

url = 'https://www.gov.br'
#tem_https, tem_br = analizar_url(url)
#print(f'Utiliza https?: {tem_https}')
#print(f'Termina com br?: {tem_br}')


# Verificar se a string contem somento numeros
def validar_idade(idade):
    idade_valida = idade.isdigit()
    if idade_valida:
        print('O valor digitado é uma idade válida')
    else:
        print('Digite somente numeros!')

#idade = input('Digite sua idade: ')
#validar_idade(idade)

# Verificar se a string contem somento letras
def validar_nome(nome):
    nome_valido = nome.isalpha()
    if nome_valido:
        print('Nome válido')
    else:
        print('Digite somente letras!')

#nome = input('Digite um nome válido: ')
#validar_nome(nome)


def validar_usuario(usuario):
    usuario_valido = usuario.isalnum()
    if usuario_valido:
        print('Usuário válido!!')
    else:
        print('Digite somente letras e números!')

#nome_usuario = input('Digite seu usuário: ')
#validar_usuario(nome_usuario)

# Analizando uma frase
def analizar_frase(frase, palavra):
    frase_limpa = frase.strip().lower()

    qtde_caracteres = len(frase_limpa)
    qtde_palavras = len(frase_limpa.split())
    ocorrencia_palavra = frase_limpa.count(palavra)

    print(f'Frase completa: {frase_limpa}')
    print(f'Total de caracteres: {qtde_caracteres}')
    print(f'Total de palavras: {qtde_palavras}')
    print(f'Ocorrencias palavra pesquisada: {ocorrencia_palavra}')

frase_input= input('Digite uma frase: ')
ocorrencia_palavra = input('Digite uma palavra para contar a ocorrencia: ')
analizar_frase(frase_input, ocorrencia_palavra)