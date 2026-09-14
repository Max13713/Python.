from random import randint
def sorteia(list):
    print('sorteando 5 valores da lista:', end=' ')
    for i in range(0, 5): 
        numero = randint(0, 10)
        list.append(numero)
        print(numero, end=' ')
    print('PRONTO!')
def somaPar(lista):
    print(f'somando os valores pares de {lista}', end=' ')
    par = list()
    for v in lista:
        if v % 2 == 0:
            par.append(v)
    print(f'temos {sum(par)}')      

numeros = list()
sorteia(numeros)
somaPar(numeros)
