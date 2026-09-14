num = soma = 0
numeros = []
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    numeros.append(num)
print(f'a soma dos {len(numeros)} foi {sum(numeros)}!')