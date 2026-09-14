idadel = []
sexol = []
maior = []
maiorf = []
while True:
    print('-' * 30)
    print(f'{'cadastre uma pressoa':^30}')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().upper()
    if sexo not in 'FM':
        while sexo not in 'FM':
            sexo = str(input('Sexo: ')).strip().upper()
    if idade > 18:
        maior.append(idade)
    else:
        idadel.append(idade)
    if sexo == 'F' and idade < 20:
        maiorf.append(idade)
    sexol.append(sexo)
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
    else:
        while cont not in 'SN':
            cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('======= Fim Do Programa =======')
print(f'Total de pessoas com mais de 18 anos: {len(maior)}')
print(f'Ao todo temos {sexol.count('M')} homens cadastrados')
print(f'E temos {len(maiorf)} mulher com menos de 20 anos')
