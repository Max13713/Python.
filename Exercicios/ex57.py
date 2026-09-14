sexo = str(input('Informe seu sexo [F/M]: ')).upper().strip()[0]
while sexo not in 'FM':
        sexo = str(input('Dados Invalidos. Por favor, Informe seu sexo [F/M]: ')).upper().strip()
print(f'sexo {sexo} registrado com sucesso')