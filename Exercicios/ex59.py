from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('segundo valor: '))
opçao = 0
print('-=-' * 10)
while opçao != 5:
    print(' [1] somar')
    print(' [2] multiplicar')
    print(' [3] maior')
    print(' [4] novos numeros')
    print(' [5] sair do programa')
    opçao = int(input('>>>>> Qual e a opçao? '))
    print('-=-' * 10)
    if opçao == 1: #somar num1 e num2
        print(f'a soma entre {num1} + {num2} e {num1 + num2}')
        print('-=-' * 10)
        sleep(2)
    elif opçao == 2:
        print(f'o resultado de {num1} * {num2} e {num1 * num2}')
        print('-=-' * 10)
        sleep(2)
    elif opçao == 3:
        print(f'entre {num1} e {num2} o maior valor e {max(num1, num2)}')
        print('-=-' * 10)
        sleep(2)
    elif opçao == 4:
        print('Informe os numeros novamente: ')
        sleep(.5)
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('segundo valor: '))
        print('-=-' * 10)
        sleep(2)
    elif opçao == 5:
        sleep(0.4)
        print('finalizando...')
        sleep(1.6)
        print('-=-' * 10)
        print('fim do programa! Volte sempre!')
        print('-=-' * 10)
    else:
        sleep(.6)
        print('opçao invalida. Tente Novamente')
        print('-=-' * 10)
    