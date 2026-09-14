pessoas = list()
dados = dict()
cont = str()
while True:
    nome = str(input('digite seu nome: ')).strip()
    idade = int(input('digite sua idade: '))
    sexo = str(input('digite seu sexo [M/F]: ')).strip().upper()[0]
    altura = float(input('digite sua altura: '))
    peso = float(input('digite seu peso: '))
    dados = dict({
        'nome':nome,
        'idade':idade,
        'sexo':sexo,
        'altura':altura,
        'peso':peso
    })
    pessoas.append(dados.copy())
    cont = str(input('Quer Continuar? [S/N]: ')).strip().upper()
    if cont == 'N':
        break
    else:
        while cont not in 'SN':
            cont = str(input('Quer Continuar? [S/N]: ')).strip()
for n, p in enumerate(pessoas):
    print(f'a {p['nome']} tem {p['idade']} anos')
