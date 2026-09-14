print('-=-' * 10)
print('Gerador de PA')
print('-=-' * 10)
t = int(input('Primeiro Termo: '))
r = int(input('Razao: '))
c = t
while c < 50:
    print(c, end=' -> ')
    c += r
print('FIM')
