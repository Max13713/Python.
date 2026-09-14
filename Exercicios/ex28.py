from time import sleep
from random import randint
print('-=-' * 20)
print('Vou Pensa em um Numero Entre 0 e 5, Tenta Adivinhar...')
print('-=-' * 20)
numA = int(randint(0, 5))
num = int(input('Qual Foi o Numero Que Eu Escoli?: '))
print('processando....')
sleep(3)
if numA == num:
    print('Parabens Vc Venceu!')
else:
    print(f'O Numero Escolhido Foi {numA}, O computador venceu!')