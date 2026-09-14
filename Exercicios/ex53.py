frase = str(input('Digite uma frase: ')).strip().replace(' ', '').upper()
invertida = frase[::-1]
print(f'O inverso de {frase} e {invertida}')
if frase == invertida:
    print('a frase digitada e um palindromo')
else:
    print('a frase digitada nao e um palindromo')