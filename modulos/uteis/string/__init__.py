def escreva(text='text', linha='~'):
    print(linha * (len(text) + 4))
    print(f'  {text}  ')
    print(linha * (len(text) + 4))

def leiaInt(msg):
    while True:
        n = input(msg).strip()
        if n.isnumeric():
            return int(n)
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
