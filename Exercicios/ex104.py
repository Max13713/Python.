def leiaInt(msg):
    while True:
        n = input(msg).strip()
        if n.isnumeric():
            return int(n)
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
n = leiaInt('digite: ')

