numb = int(input('Digite um numero: '))
total = 0
for c in range(1, numb + 1):
    if numb % c == 0:
        total += 1
if total == 2:
    print('ele e primo')
else:
    print('ele nao e primo')
