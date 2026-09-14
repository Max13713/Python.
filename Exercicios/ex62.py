print('-=-' * 10)
print('Gerador de PA')
print('-=-' * 10)
t = int(input('Primeiro Termo: '))
r = int(input('Razao: '))
total = 0
mais= 10
cont = 1
while mais != 0:
    total += mais
    while cont <= total:
        print(t, end=' -> ')
        t += r
        cont += 1
    print('Pausa')
    mais = int(input('quantos termos a mais vc quer mostra? '))
    cont + 1
    
print('fim')
