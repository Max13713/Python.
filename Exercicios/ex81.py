lista = list()
valor = int
cont = str
while True:
    valor = int(input('digite um numero: '))
    lista.append(valor)
    cont = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
    else:
        while cont not in 'SN':
            cont = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
print('-=-' * 15)
print(f'vc digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'os valores em ordem decresente sao {lista}')
if 5 in lista:
    print('o valor 5 faz parte da lista!')
else:
    print('o valor 5 nao foi encontrado na lista!')