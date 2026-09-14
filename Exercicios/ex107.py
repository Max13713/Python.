from mex107 import moeda

p = float(input('Digite o preço: R$'))
print(f'a metade de {p} e {moeda.metade(p)}')
print(f'o dobro de {p} e {moeda.dobro(p)}')
print(f'aumentando 10% de {p} e {moeda.aumentar(p, 10)}')
print(f'reduzindo 13% de {p} e {moeda.diminuir(p, 13)}')