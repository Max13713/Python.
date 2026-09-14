from datetime import date
ano = int(input('que anoo vc quer analisar? coloque 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'o ano {ano} e Bissexto')
else:
    print(f'o ano {ano} Nao e Bissexto')