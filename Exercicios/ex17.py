from math import hypot
catetoO = float(input('comprimento do cateto oposto?: '))
catetoA = float(input('comprimento do cateto adjacente?: '))
hipotenusa = hypot(catetoO, catetoA)
print(f'a hipotenusa e {hipotenusa:.2f}')