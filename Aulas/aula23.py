try:
    a = int(input('Numero a:'))
    b = int(input('Numero b:'))
    r = a / b
except (ValueError, TypeError):
    print('Tivemes um problem com os tipos de dados que yocė digitou.')
except ZeroDivisionError:
    print('nao e possivel dividir por zero')
except KeyboardInterrupt:
    print('o usuario preferiu nao informar os dados')
else:
    print(r)
finally:
    print('volte sempre!')
