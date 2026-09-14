tabuada = 0
print('-' * 40)
print('Digite uma valor negativo para sair.')
print('-' * 40)
while True:
    tabuada = int(input('Quer Ver a tabuada de qual valor? '))
    print('=' * 40)
    if tabuada < 0:
        print('Tabuada encerrada.')
        break
    for c in range(1,10 + 1):
        r = tabuada * c
        print(f'{tabuada} x {c:2} = {r}')
    print('=' * 40)