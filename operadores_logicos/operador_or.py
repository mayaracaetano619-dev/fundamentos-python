# Operador or

def posso_comprar():
    TEM_CARTAO = False
    tem_dinheiro = bool(input('Você tem dinheiro para comprar?'))
    autorizado = tem_dinheiro or TEM_CARTAO
    print(f'Vou comer um MC-Donalds hoje? {autorizado}')

posso_comprar()
