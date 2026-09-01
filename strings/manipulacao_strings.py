# Converter texto para maiúsculas e minúsculas
def formatar_nome(nome):
    # nome maiúsculo:
    nome_maiuscula = nome.upper()

    # nome manúsculo:
    nome_minuscula = nome.lower()

    # nome com primeira letra maiúcula:
    nome_camel_case = nome_maiuscula.capitalize()

    return nome_maiuscula, nome_minuscula, nome_camel_case

nome = input('Digite seu nome: ')

nome_maiuscula, nome_minuscula, nome_camel_case = formatar_nome(nome)
print(f'Nome maiúsculo: {nome_maiuscula}')
print(f'Nome minúscula: {nome_minuscula}')
print(f'Nome camel-case: {nome_camel_case}')


# Remover espaços desnecessários
def limpar_texto(texto):
    #Remove espaços no início e final do texto
    texto_limpo = texto.strip()
    # Remove espaços da esquerda .lstrip()
    # Remove espaços da direita .rstrip()
    return texto_limpo

texto_1 = '    Aprender Python é legal!      '
print(f'Texto original: {texto_1}')
print(f'Texto editado: {limpar_texto(texto_1)}')

# Substituir Palavras
def trocar_cidade (texto):
    # Troca uma palavras por outra
    texto_trocado = texto.replace('São Paulo', 'Piracicaba')
    return texto_trocado

cidade = 'Eu moro em São Paulo'
print(trocar_cidade(cidade))

# Contar caracteres ou ocorrencias
def analizar_texto(texto, letra):
    #contar a quantidade de caracteres
    qtde_caracteres = len(texto)

    #contar a quantidade de ocorencias
    qtde_letra_a = texto.strip().lower().count(letra)

    return qtde_caracteres, qtde_letra_a

text_2 = input('Digite seu texto: ')
letra = input('Digite uma letra: ')
caracteres, letras_a = analizar_texto(text_2,letra)

print(f'Total de caracteres: {caracteres}')
print(f'Total de letras  pesquisadas: {letras_a}')

# Verificar se uma palavra está presente
def verificar_palavra(frase, palavra):
    palavra_presente = palavra.lower() in frase.lower()
    # Retorna um booleano (True ou False)
    return palavra_presente

frase = input('Digite uma frase: ')
palavra = input('Digite uma palavra: ')

print(f'A palavra está presente na frase? {verificar_palavra(frase, palavra)}')

# Encontrar a posição da uma palavra
def encontrar_posicao_palavra(frase, palavra):
    posicao_palavra = frase.lower().find(palavra.lower())
    return posicao_palavra

frase_2 = input('Digite uma nova frase: ')
palavra_2 = input('Digite uma palavra para saber sua posicao: ')

print(f'A posição da palavra é {encontrar_posicao_palavra(frase_2, palavra_2)}')