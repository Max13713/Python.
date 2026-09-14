from mex108 import moeda

p = float(input('Digite o preço: R$'))
print(f'a metade de {moeda.moeda(p)} e {moeda.moeda(moeda.metade(p))}')
print(f'o dobro de {moeda.moeda(p)} e {moeda.moeda(moeda.dobro(p))}')
print(f'aumentando 10% de {moeda.moeda(p)} e {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'reduzindo 13% de {moeda.moeda(p)} e {moeda.moeda(moeda.diminuir(p, 13))}')