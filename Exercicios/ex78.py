lista = list()
for v in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posiçao {v}: ')))
maior= max(lista)
menor = min(lista)
print('-=-' * 40)
print(f'vc digitou os valores {lista}')
print(f' o maior valor digitado foi {maior} nas posiçoes ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print(f' o menor valor digitado foi {menor} nas posiçoes ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
