def salario():
    valor_hora = int(input('Digite o valor da hora trabalhada: '))
    horas = int(input('Digite a quantidade de horas trabalhadas: '))

    salario = valor_hora * horas

    print(f'O salário é: R$ {salario:}')



salario()