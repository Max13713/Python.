galera = list()
dado = list()
for c in range(0, 3):
    dado.append (str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} e maior de idade.') 
    else:
        print(f'{p[0]} nao e maior de idade')