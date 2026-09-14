matriz = list([[0, 0, 0], [0, 0, 0], [0, 0, 0], [], [], []])
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            matriz[3].append(matriz[l][c])
        if l == 1:
            matriz[4].append(matriz[l][c])
        if c == 2:
            matriz[5].append(matriz[l][c])
print('-=' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:^5} ]', end='')
    print()
print('-=' * 20)
print(f'a soma dos valores pares e {sum(matriz[3])}')
print(f'a soma dos valoores da terceira coluna e {sum(matriz[5])}')
print(f'o maior valor da segunda linha e {max(matriz[4])}')
