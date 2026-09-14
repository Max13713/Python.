from datetime import datetime
def voto(a=0):
    idade = abs(datetime.now().year - a)
    if idade <= 18:
        return (f'com {idade} anos: {'NAO VOTA.'}')
    elif idade <= 65 and idade >= 18:
        return (f'com {idade} anos: {'VOTO OBRIGATORIO.'}')
    else:
        return (f'com {idade} anos: {'VOTO OPCIONAL.'}')
data = int(input('em que ano vc nasceu? '))
print(voto(data))
