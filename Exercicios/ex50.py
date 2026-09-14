q = 0
p = 0
for c in range(0, 6):
    n = int(input('Digite uma numero: '))
    if n % 2 == 0:
        q += 1
        p += n
print(f'voce informou {q} numeros pares e a soma foi de {p}')