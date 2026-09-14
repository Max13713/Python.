from time import sleep
def lin(est, tam):
    print(f'{est}' * tam)
def contador(i, f, p):
    lin('-=', 20)
    if p == 0:
        p = 1
    print(f'contagem de {i} ate {f} de {p} em {p}')
    if i <= f:
        for v in range(i, f + 1, p):
            print(v, end=' ')
    elif i >= f:
        p = -abs(p)
        for v in range(i, f - 1, p):
            print(v, end=' ')
    print('Fim!')
contador(1, 10, 1)
contador(10, 0, 2)
print('agora e sua vez de personaliza a contagem!')
contador(int(input('inicio: ')),
         int(input('fim:    ')),
         int(input('passo:  ')))
