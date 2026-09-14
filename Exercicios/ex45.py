from random import randint
from time import sleep
print('Suas opçoes:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
listaop = ['Pedra', 'Papel', 'Tesoura','Sla']
veri = [0, 1, 2]
jogador = int(input('Qual a sua jogada? '))
computador = randint(0, 2)
quven = str
if jogador == computador:
    quven = str('empate'.upper())
elif jogador == 0 and computador == 2:
    quven = str('jogador'.upper())
elif jogador == 1 and computador == 0:
    quven = str('jogador'.upper())
elif jogador == 2 and computador == 1:
    quven = str('jogador'.upper())
else:
    if jogador in veri:
        quven = str('computador'.upper())
    else:
        print('JOGADA INVALIDA!')
        quit()
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)
print('-=-' * 10)
print(f'computador jogou {listaop[computador]}')
print(f'jogador jogou {listaop[jogador]}')
print('-=-' * 10)
if quven == 'EMPATE ':
    print(f'Deu {quven.upper()}')
else:
    print(f'{quven.upper()} VENCE') 
    