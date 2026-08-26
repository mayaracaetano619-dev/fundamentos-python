def criar_ranking(pontuacoes):
    ranking = sorted(pontuacoes, reverse=True)
    print(f'Ranking: {ranking}')
pontuacoes = []
while True:
    pontuacao = int(input('Digite uma pontuação ou 0 para parar: '))
    if pontuacao == 0:
        break
    pontuacoes.append(pontuacao)


criar_ranking(pontuacoes)