lista = list([])
num = int(0)
for c in range(0, 5):
    num += 1
    peso = float(input(f'peso da {num} pessoa: '))
    lista.append(peso)
print(f'O maior peso lindo foi {max(lista)}Kg')
print(f'O menor peso lindo foi {min(lista)}Kg')
