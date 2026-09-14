nomes = []
preços = []
soma = float(0)
quant = int(0)
while True:
    print('-' * 30)
    print(f'{'Mercadao':^30}')
    print('-' * 30)
    nomep = str(input('Nome do Produto: ')).strip().upper()
    preçop = int(input('Preço: '))
    nomes.append(nomep)
    preços.append(preçop)
    soma += preçop
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
    else:
        while cont not in 'SN':
            cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
for c in preços:
    if c > 1000:
        quant += 1
print('======= Fim Do Programa =======')
print(f'o total da compra foi de R${soma:.2f}')
print(f'Temos {quant} produtos custando mais de R$1000.00')
print(f'o produto mais barato foi {nomes[preços.index(min(preços))]} que custa R${min(preços)}')
