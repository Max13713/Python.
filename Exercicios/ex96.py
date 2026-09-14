def area(l, c):
    a = l * c
    print(f'a area do terreno {l}x{c} e de {a}m²')
print()
print('controle de terreno')
print('-' * 15)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
