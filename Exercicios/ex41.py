from datetime import date
nasc = int(input('ano de nascimento: '))
idade = date.today().year - nasc
print(f'o atleta tem {idade} anos.')
if idade <= 9:
    print('classificaçao: MIRIM')
elif idade <= 14:
    print('classificaçao: INFANTIL')
elif idade <= 19:
    print('classificaçao: JUNiOR')
elif idade <= 25:
    print('classificaçao: SENIOR')
else:
    print('classificaçao: MASTER')