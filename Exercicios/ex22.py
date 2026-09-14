nome = (input('Digite Seu Nome Completo: ')).strip()
print(f'todas as letras maiusculas {nome.upper()}')
print(f'todas as letras minusculas {nome.lower()}')
print(f'Total de letras sem espaços {len(nome) - nome.count(' ')}')
print(f'quantidade de letras do primeiro nome {len(nome.split()[0])}')



