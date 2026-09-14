from random import randint
from time import sleep
print('-' * 30)
print(f'{'Mega da virada':^30}')
print('-' * 30)
while True:
    jogos = int(input('Quantos jogos vc quer que eu sorteie? '))
    if jogos == 0:
        print('Nao tem como sortear 0 jogos')
    else:
        break
matriz = list([])
nuns = list()
cont = 0
for l in range(jogos):
    while True:
        num = int(randint(0, 60))
        if num not in nuns:
            nuns.append(num)
            cont += 1
        if cont >= 6:
            break
    matriz.append(sorted(sorted(nuns[:])))
    cont = 0
    nuns.clear()
print(f'-=-=-= Sorteando {jogos} {'jogos' if jogos > 1 else 'jogo'} =-=-=-')
for j in matriz:
    print(f'Jogo {matriz.index(j) + 1}: {j}')
    sleep(1)
print('-=-=-=-=-=-= Boa Sorte! =-=-=-=-=-=-')
