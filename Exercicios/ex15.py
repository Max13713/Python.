dias = int(input('Quantos dias alugado?: '))
km = float(input('Quantos km rodado?: '))
total = dias * 60 + km * 0.15
print(f'o total a pagar e de {total:.2f}')