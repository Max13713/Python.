def leiaInt(msg = 0):
    while True:
        try:
            n = int(input(msg).strip())
        except KeyboardInterrupt:
            print('\033[31mUsuario preferiu nao digitar esse numero.\033[m')
            return 0
        except:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        else:
            return int(n)
def leiaFloat(msg = 0):
    while True:
        try:
            n = float(input(msg).strip())
        except KeyboardInterrupt:
            print('\033[31mUsuario preferiu nao digitar esse numero.\033[m')
            return 0
        except:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        else:
            return float(n)
n = leiaInt('digite um inteiro: ')
r = leiaFloat('digite um real: ')
print(f'o valor inteiro digitado foi de {n} e o real foi {r}')