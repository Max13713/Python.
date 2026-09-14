from datetime import datetime
dados = dict({
    'nome':'teste',
    'idade':0,
    'ctps':0,
})
dados['nome'] = str(input('nome: '))
dados['idade'] = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - dados['idade']
abs(dados['idade'])
ctps = int(input('Carteira de trabalho (0 nao tem): '))
if ctps != 0:
    dados['contrataçao'] = int(input('ano de contrataçao: '))
    dados['salario'] = float(input('Salario: '))
    dados['aposentadoria'] = (dados['contrataçao'] + 35 - datetime.now().year) + dados['idade']
    abs(dados['contrataçao'])
print('-=' * 20)
print(dados)
print(f'o nome tem o valor {dados['nome']}')
print(f'idade tem o valor {dados['idade']}')
print(f'ctps tem o valor {dados['ctps']}')
if ctps != 0:
    print(f'contrataçao tem o valor {dados["contrataçao"]}')
    print(f'salario tem o valor {dados['salario']}')
    print(f'aposentadoria tem o valor {dados['aposentadoria']}')