from datetime import date
data = 0
num = 0
cmaior = 0
cmenor = 0
for c in range(0, 7):
    num = num + 1
    data = int(input(f'Em que ano a {num} pessoa nasceu? '))
    idade = data - date.today().year
    if abs(idade) < 21:
        cmenor += 1
    else:
        cmaior += 1
print(f'ao todo tivemos {cmaior} pessoas maiores de idade')
print(f'ao todo tivemos {cmenor} pessoas menores de idade')
