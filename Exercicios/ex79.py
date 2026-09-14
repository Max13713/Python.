lista = list()
valor = int
cont = ''
while True:
    valor = int(input('Digite um valor '))
    if valor not in lista:
        print('valor adicionado com sucesso...')
        lista.append(valor)
    else:
        print('valor duplicado! nao vou adicionar...')
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
    else:
        while cont not in 'SN':
            cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('-=-' * 15)
print(f'Vc digitou os valores {lista}')