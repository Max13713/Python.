def dobro(n = 1, f=False):
    n = n * 2
    if f == True:
        n = str(f'R${n:.2f}')
        return n
    else:
        return n
def metade(n = 1, f=False):
    n /= 2
    if f == True:
        n = str(f'R${n:.2f}')
        return n
    else:
        return n
def aumentar(n = 1, a=1, f=False):
    p = n * a / 100
    n += p
    if f == True:
        n = (f'R${n:.2f}')
        return n
    else:
        return n
def diminuir(n=1, a=1, f=False):
    p: float | int = n * a / 100
    n -= p
    if f == True:
        n = (f'R${n:.2f}')
        return n
    else:
        return n
def moeda(n = 1, f=False):
    if f == True:
        n = (f'R${n:.2f}')
        return n
    else:
        return n
def resumo(preço, aumento=10, reduçao=10):
    print('-' * 40)
    print(f'{'RESUMO DO VALOR':^40}')
    print('-' * 40)
    print(f'preço analisado: \t{moeda(preço)}')
    print(f'dobro do preço: \t{dobro(preço, True)}')
    print(f'metade do preço: \t{metade(preço, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preço, aumento, True)}')
    print(f'{reduçao}% de reduçao: \t{diminuir(preço, reduçao, True)}')