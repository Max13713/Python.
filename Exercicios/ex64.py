num = soma = cont = 0
num = int(input('Digite um numero: '))
while num != 999:
    soma += num 
    cont += 1
    num = int(input('Digite um numero: '))
print(f'vc digitou {cont} numeros e a soma entre eles foi de {soma}')
