km = float(input('Qual a Velocidade Do Carro?: '))
if km > 80:
    vm = (km - 80) * 7
    print(f'MULTADO! Vc excedeu o limite permitido de 80km/h\nvc deve pagar uma multa de R${vm:.2f}')
else:
    print('Tenha Um Otimo Dia!')