def linha(tam = 42):
    return '-' * tam
def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg).strip())
        except KeyboardInterrupt:
            print('\033[31mUsuario preferiu nao digitar esse numero.\033[m')
            return 3
        except:
            print('\033[31mERRO! Digite uma opçao valida!.\033[m')
            continue
        else:
            return n
def sair():
    cabeçalho('Saindo do sistema... ate logo!')
def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - {item}')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opçao: \033[m')
    return opc