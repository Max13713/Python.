n = int(input('Quantos termos vc quer mostrar? '))
n1 = 0
n2 = 1
print(f'{n1} -> {n2} ', end='')
cont = 3
while cont <= n:
    n3 = n1 + n2
    print(f' -> {n3} ', end='')
    cont += 1
    n1 = n2
    n2 = n3
    