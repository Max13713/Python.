numex = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if num <= 20 and num >= 0:
        print(f'vc digitou o numero {numex[num]}')
        break
    else:
        pass
    