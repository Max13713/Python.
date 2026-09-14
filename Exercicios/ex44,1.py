print('-=-' * 20)
print('Lojas Super Guanabara')
print('-=-' * 20)
preço = float(input('Preço das compras: R$'))
print('[ 1 ] a vista dinheiro/cheque')
print('[ 2 ] no cartao')
forpag = int(input('Qual e a opçao? '))
preçfinal = float
if forpag == 1:
    preçfinal = preço - preço * 10 / 100
    print(f'Sua compra de R${preço:.2f} vai custar R${preçfinal:.2f} no final')
else:
    print('[ 1 ] debito')
    print('[ 2 ] credito')
    tpcar = int(input('Qual e a opçao? '))
    if tpcar == 1:
        preçfinal = preço - preço * 5 / 100
        print(f'Sua compra de R${preço:.2f} vai custar R${preçfinal:.2f} no final')
    else:
        parcelas = int(input('Quantas parcelas? '))
        if parcelas > 4:
            preçofinal = preço + preço * (20 + (parcelas - 4)) / 100
            preçoparc =  preçofinal / parcelas
            print(f'sua compra sera parcelada em {parcelas}x de R${preçoparc:.2f} COM JUROS')
            print(f'sua compra de R${preço:.2f} vai custar R${preçofinal:.2f} no final.')
        else:
            preçoparc =  preço / parcelas
            print(f'Sua compra sera pacelada em {parcelas}X de R${preçoparc} SEM JUROS')
