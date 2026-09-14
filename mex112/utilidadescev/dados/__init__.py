def leiadinheiro(msg):
    while True:
        entrada = str(input(msg)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO: "{entrada}" e um preço inválido.\033[m')
        else:
            return float(entrada)
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
