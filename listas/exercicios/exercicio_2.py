def inserir_aluno(alunos, nome, posicao):
    alunos.insert(posicao, nome)
    print(f'Lista de alunos: {alunos}')


alunos = ['Mayara', 'Sophia', 'Nicolas', 'David', 'Laura']

nome = input('Digite o nome do aluno: ')
posicao = int(input('Digite a posição do aluno: '))

inserir_aluno(alunos, nome, posicao)