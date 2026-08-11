def cadastro():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    profissao = input("Digite sua profissão: ")
    cidade = input("Digite sua cidade: ")

    print("====== CADASTRO ======")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Profissão: {profissao}")
    print(f"Cidade: {cidade}")
    print("======================")


cadastro()