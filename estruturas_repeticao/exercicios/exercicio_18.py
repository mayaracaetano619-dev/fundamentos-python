def caixa_eletronico():
    valor = int(input("Digite o valor que deseja sacar: "))
    notas = [100, 50, 20, 10, 5, 2]

    for nota in notas:
        quantidade = valor / nota

        if quantidade > 0:
            print(f"Notas de {nota}: {quantidade}")

        valor = valor % nota

caixa_eletronico()