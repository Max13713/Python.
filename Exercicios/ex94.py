pessoas = list()
dados = dict({})
media = list()
while True:
    dados.clear
    dados['nome'] = str(input('Nome: '))
    dados['idade'] = int(input('Idade: '))
    while True:
        dados['sexo'] = str(input('Sexo: [F/M] ')).strip().upper()
        if dados['sexo'] in 'MF':
            break
        print('ERRO! por favor, digite apenas F ou M')
    media.append(dados['idade'])
    pessoas.append(dados.copy())
    while True:
        cont = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
        if cont in 'SN':
            break
        print('ERRO! por favor, digite apenas S ou N')
    if cont == 'N':
        break
media = sum(media) / len(media)
print('-=' * 20)
print(f'- o grupo tem {len(pessoas)} pessoas.')
print(f'- a media de idade e de {media:5.2f} anos.')
print(f'- as mulheres cadastradas foram:', end=' ')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p['nome']} ', end='')
print()
print('- lista das pessoas que estao acima da media: ')
for p in pessoas:
    if p['idade'] >= media:
        print('      ')
        for k, v in p.items():
            print(f'  - {k} = {v}; ', end=' ')
        print()