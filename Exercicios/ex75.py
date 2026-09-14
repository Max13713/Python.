numbs = (int(input('Digite um numero: ')), 
         int(input('Digite outro numero: ')), 
         int(input('Digite mais um numero: ')), 
         int(input('Digite o ultimo numero: ')))
print(f'o valor 9 apareceu {numbs.count(9)} vezes')
if 3 in numbs:
    print(f'o valor 3 apareceu na {numbs.index(3) + 1} posiçao')
else:
    print('o valor 3 nao foi digitado em nenhuma posiçao')
print('os valores pares digitados foram ', end='')
for pos, num in enumerate(numbs):
    if num % 2 == 0:
        if pos == len(numbs) - 1:
            print(num)
        else:
            print(num, end=' ')