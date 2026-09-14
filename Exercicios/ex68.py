from random import randint
vitorias = int(0)
ven = str
pi = str
ip = str
jogador = soma =int(0)
computador = int(0)
while True:
    print('-=-' * 10)
    jogador = int(input('Digite uma valor: '))
    pi = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    computador = randint(0, 10)
    soma = jogador + computador
    if soma % 2 == 0:
        ip = 'P'
    else:
        ip = 'I'
    if pi == ip:
        ven = 'J'
    else:
        ven = 'C'
    print('-' * 30)
    print(f'vc jogou {jogador} e o computador {computador}. Total {soma} DEU {'IMPAR' if ip == 'I' else 'PAR'}')
    print('-' * 30)
    print('Vc VENCEU!' if ven == 'J' else 'Vc PERDEU!')
    if ven == 'J':
        vitorias += 1
        print('Vamos Jogar Novamente...')
    else:
        print('-=-' * 10)
        print(f'GAMER OVER! vc venceu {vitorias} vezes.')
        break  
