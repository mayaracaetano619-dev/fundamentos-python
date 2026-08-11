def comissao():
    salario_fixo = int(input("Digite o salário fixo: R$ "))
    vendas = int(input("Digite o valor das vendas: R$ "))
    percentual = int(input("Digite o percentual de comissão: "))

    comissao = vendas * percentual / 100
    salario_final = salario_fixo + comissao

    print(f"Valor da comissão: R$ {comissao:}")
    print(f"Salário final: R$ {salario_final:}")


comissao()