numbs = list([[], []])
num = int
for n in range(1, 6):
    num = (int(input(f'Digite o {n}°. valor: ')))
    if num % 2 == 0:
        numbs[0].append(num)
    else:
        numbs[1].append(num)
print(f'os valores pares digitados foram {numbs[0]}')
print(f'os valores impares digitados foram {numbs[1]}')
