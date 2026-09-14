num =  int(input('Digite um numero inteiro: '))
base = int(input('[ 1 ] para binario\n[ 2 ] para octal\n[ 3 ] para hexadecimal\nSua Opçao: '))
if base == 1:
    print(f'{num} convertido para binario e igual a {bin(num)[2:]}')
elif base == 2:
    print(f'{num} convertido para octal e igual a {oct(num)[2:]}')
elif base == 3:
    print(f'{num} convertido para hexadecimal e igual a {hex(num)[2:]}')
else:
    print('opçao invalida. Tente Novamente.')