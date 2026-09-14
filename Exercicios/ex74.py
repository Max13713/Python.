from random import randint
seq = (randint(0, 10),
       randint(0, 10),
       randint(0, 10),
       randint(0, 10),
       randint(0, 10))
print(f'os valores sorteados foram: ', end='')
for pos, num in enumerate(seq):
    if pos == len(seq) - 1:
        print(num)
    else:
        print(num, end=' ')
print(f'o maior valor sorteado foi {max(seq)}')
print(f'o menor valor sorteado foi {min(seq)}')
