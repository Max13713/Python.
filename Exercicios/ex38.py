from time import sleep
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
print('Processando...')
sleep(1)
if num1 > num2:
    print('O primeiro valor e maior')
elif num1 > num2:
    print('O segundo valor e maior')
else:
    print('Nao exste valor maior, os dois sao iguais')