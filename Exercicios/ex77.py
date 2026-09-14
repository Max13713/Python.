palavras = ('placa mae', 'processaador', 'placa de video', 'memoria ram', 'ssd', 'gabinete', 'fonte', )
for p in palavras:
    print(f'\nna palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')