salario = float(input('qual o seu salario?: '))
aumento = float

if salario > 1250:
    aumento = salario + (salario * 10 / 100)
    print(f'Seu Salario depois do aumento e de R${aumento:.2f}')
else:
    aumento = salario + (salario * 15 / 100)
    print(f'Seu Salario depois do aumento e de R${aumento:.2f}')
print(type(aumento))