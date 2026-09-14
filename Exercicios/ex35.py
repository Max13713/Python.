s1 = float(input('primeiro segmento: '))
s2 = float(input('segundo segmento: '))
s3 = float(input('terceiro segmento: '))
maior = max(s1, s2, s3)
if s1 + s2 + s3 - maior > maior:
    print('true')
else:
    print('false')
