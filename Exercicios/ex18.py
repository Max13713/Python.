from math import radians, sin, cos, tan
angulo = float(input('Um Angulo Qualquer: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print(f'o seno de {angulo}° e {sen}')
print(f'o cosseno de {angulo}° e {cos}')
print(f'o tangente de {angulo}° e {tan}')
