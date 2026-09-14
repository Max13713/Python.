from datetime import date
nasc = int(input('ano de nascimento: '))
idade = date.today().year - nasc
tempo = idade - 18
ano = date.today().year + abs(tempo)

if idade < 18:
    print(f'quem nasceu em {nasc} tem {(idade)} anos em {date.today().year}.')
    print(f'ainda faltao {abs(tempo)} anos para o alistamento.')
    print(f'seu alistamento sera {ano}.')
elif idade == 18:
    print(f'quem nasceu em {nasc} tem {(idade)} anos em {date.today().year}.')
    print(f'vc tem que se alistar IMEDIATAMENTE!')
else:
    print(f'quem nasceu em {nasc} tem {(idade)} anos em {date.today().year}.')
    print(f'vc ja deveria ter se alistado ha {tempo} anos.')
    print(f'seu alistamento foi em {date.today().year - tempo}.')
