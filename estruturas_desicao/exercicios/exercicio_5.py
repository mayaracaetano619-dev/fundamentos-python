def nota():
    nota = float(input('Digite uma nota de 0 a 10: '))

    if nota >= 0 and nota <= 4:
        print('Insuficiente')
    elif nota >= 5 and nota <= 6:
        print('Regular')
    elif nota >= 7 and nota <= 8:
        print('Bom')
    elif nota >= 9 and nota <= 10:
        print('Excelente')
    else:
        print('Nota inválida.')


nota()