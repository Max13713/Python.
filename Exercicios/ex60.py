print('digite um numero para')
num = int(input('calcular seu fatorial: '))
c = num
fatorial = 1
print(f'calculando  {num}! = ', end='')
while c > 0:
    fatorial *= c
    print(f'{c}',end='')
    print(' x ' if c > 1 else f' = {fatorial}', end='')
    c -= 1
