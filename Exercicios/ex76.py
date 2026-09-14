print('-' * 30)
print(f'{'listagem de preços':^30}')
print('-' * 30)
listagem = ('lapis', 1, 
            'borracha', 2, 
            'caderno', 20.90, 
            'compasso', 5.98)
print()
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    elif pos % 2 == 1:
        print(f'R${listagem[pos]:.>5.2f}')
print('-' * 30)
