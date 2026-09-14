s1 = float(input('primeiro segmento: '))
s2 = float(input('segundo segmento: '))
s3 = float(input('terceiro segmento: '))
maior = max(s1, s2, s3)
tipo = str
if s1 + s2 + s3 - maior > maior:
    if s1 == s2 == s3:
        tipo = str('Equilatero')
    elif s1 == s2 or s2 == s3 or s1 == s3:
        tipo = str('Isosceles')
    else:
        tipo = str('Escalendo')
    print(f'os segmentos PODEM FORMAR um tringulo {tipo}')
else:
    print('os segmentos NAO FORMAR um tringulo')