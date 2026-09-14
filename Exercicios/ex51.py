print('-=-' * 10)
print('Gerador de PA')
print('-=-' * 10)
t = int(input('Primeiro Termo: '))
r = int(input('Razao: '))
for c in range(t, 50, r):
    print(c, end=' -> ')
print('acabou')
