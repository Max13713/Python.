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
