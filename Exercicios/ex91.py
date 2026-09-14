from random import randint
from time import sleep
from operator import itemgetter
jogador = dict({
    'jogador1':randint(1, 6),
    'jogador2':randint(1, 6),
    'jogador3':randint(1, 6),
    'jogador4':randint(1, 6)
})
ranking = dict({})
print('Valores Sorteados: ')
for k, v in jogador.items():
    print(f'  - o {k} tirou {v}')
    sleep(.5)
print('Ranking dos jogadores:')
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'  {i+1} lugar: {v[0]} com {v[1]}')
    sleep(1)