from time import sleep
def escreva(text):
    print('~' * (len(text) + 4))
    print(f'  {text}  ')
    print('~' * (len(text) + 4))
def helpp(n):
    sleep(.3)
    escreva(f'acessando o manual do comando {n}')
    sleep(.7)
    help(n)
    sleep(1)
while True:
    escreva('SISTEMA DE AJUDA PyHELP')
    commando = str(input('Funcao ou bliblioteca > ')).strip().lower()
    if commando == 'fim':
        break
    helpp(commando)
sleep(.5)
escreva('ATE LOGO!')
