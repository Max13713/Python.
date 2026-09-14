media = float
num = 0
resp = str('S')
numeros = []
while resp == 'S':
    num = int(input('digite um numero: '))
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    numeros.append(num)
media = sum(numeros) / len(numeros)
print(f'vc digitou {len(numeros)} numeros e a media foi {media:.2f}')
print(f'o maior valor foi de {max(numeros)} e o menor foi {min(numeros)}')
    