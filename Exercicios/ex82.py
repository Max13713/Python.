numbs = list()
par = list()
impar = list()
num = int
cont = str
while True:
    num = int(input('digite um numero: '))
    numbs.append(num)
    cont = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
    else:
        while cont not in 'SN':
            cont = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
for v in numbs:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print('-=-' * 15)
print(f'a lista completa e {numbs}')
print(f'a lista de pares e {par}')
print(f'a lista de impares e {impar}')