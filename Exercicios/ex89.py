boletim = list()
dados = list()
cont = str
while True:
    nome = (str(input('Nome: ')))
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    media = (nota1 + nota2) / 2
    dados = list([nome, [nota1, nota2], media])
    boletim.append(dados[:])
    cont = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
    else:
        while cont not in 'SN':
            cont = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
print('-=-' * 20)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-' * 30)
num = 0
while num != 999:
    num = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if num <= len(boletim) - 1:
        print(f'Notas de {boletim[num][0]} São {boletim[num][1]}')
    else:
        print(f'Invalido. nao tem aluno {num}')
    print('-' * 30)
print('FIM DO PROGRAMA')
