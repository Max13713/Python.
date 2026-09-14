altura = float(input('Qual a sua altura? (m) '))
peso = float(input('Quantos kilos vc tem? (Kg) '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('vc esta abaixo do peso normal')
elif imc > 18.5 and imc <= 25:
    print('vc esta na faixa de peso normal')
elif imc > 25 and imc <= 40:
    print('vc esta em sobrepeso')
elif imc > 30 and imc <= 40:
    print('vc esta em obesidade')
else:
    print('vc esta em obesidade morbita')
