print('-=-' * 20)
print(f'{" Lojas Super Gunabara ":=^40}')
print('-=-' * 20)
preço = float(input('Preço das compras: R$'))
print('[ 1 ] a vista dinheiro/cheque')
print('[ 2 ] a vista cartao')
print('[ 3 ] 2x cartao')
print('[ 4 ] 3x ou mais no cartao')
forpag = int(input('Qual e a opçao? '))
preçfinal = float
if forpag == 1:
    preçfinal = preço - preço * 10 / 100
    print(f'Sua compra de R${preço:.2f} vai custar R${preçfinal:.2f} no final')
elif forpag == 2:
    preçfinal = preço - preço * 5 / 100
    print(f'Sua compra de R${preço:.2f} vai custar R${preçfinal:.2f} no final')
elif forpag == 3:
    preçoparc =  preço / 2
    print(f'Sua compra sera pacelada em 2X de R${preçoparc} SEM JUROS')
    print(f'sua compra de R${preço:.2f} vai custar R${preçoparc:.2f} no final.')
elif forpag == 4:
    parcelas = int(input('Quantas parcelas? '))
    preçofinal = preço + preço * 20 / 100
    preçoparc =  preçofinal / parcelas
    print(f'sua compra sera parcelada em {parcelas}x de R${preçoparc} COM JUROS')
    print(f'sua compra de R${preço:.2f} vai custar R${preçofinal:.2f} no final.')
else:
    print('opçao invalida. tente novamente')
    