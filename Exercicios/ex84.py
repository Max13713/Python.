pessoas = list()
dados = list()
mai = men= 0
cont = str
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados [1]
        if dados[1] < men:
            men = dados [1]
    pessoas.append(dados[:])
    dados.clear()
    cont = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
    else:
        while cont not in 'SN':
            cont = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
print('-=' * 20)
print(f'ao todo vc cadastrou {len(pessoas)} pessoas.')
print(f'o maior peso foi de {mai}Kg. peso de ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print(f'\no menor peso foi de {men}Kg. peso de ', end='')
for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')

