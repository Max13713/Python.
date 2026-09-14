from mex109 import moeda

p = float(input('Digite o preço: R$'))
print(f'a metade de {moeda.moeda(p, True)} e {moeda.metade(p, True)}')
print(f'o dobro de {moeda.moeda(p, True)} e {moeda.dobro(p, True)}')
print(f'aumentando 10% de {moeda.moeda(p, True)} e {moeda.aumentar(p, 10, True)}')
print(f'reduzindo 13% de {moeda.moeda(p, True)} e {moeda.diminuir(p, 13, True)}')