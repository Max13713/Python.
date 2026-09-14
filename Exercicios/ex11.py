largura = float(input('qual a largura da parede?: '))
altura = float(input('qual o altura da parede?: '))
area = largura * altura
tinta = area / 2
print(f'Sua parede tem a dimensao de {largura}x{altura} e sua area e de {area}m².\nPara pintar essa parede, vc vai precisara de {tinta}l de tinta.')