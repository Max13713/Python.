from random import randint
print('-=-' * 20)
print('Pensei em um Numero Entre 0 e 10...')
print('Sera que vc consegue adivinhar qual foi?')
print('-=-' * 20)
palpite = int(input('Qual e seu palpite? '))
num = int(randint(0, 10))
tentativas = 1
while palpite != num:
    tentativas += 1
    if palpite < num:
        print('Mais... Tente mais uma vez.')
    else:
        print('Menos... Tente mais uma vez.')   
    palpite = int(input('Qual e seu palpite? '))
print(f'voce acertou com {tentativas} tentativas. parabens!')