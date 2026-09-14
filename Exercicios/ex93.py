dados = dict({
    'nome':'teste',
    'total':0
})
partidas = list()
dados['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas Partidas {dados['nome'].capitalize()} jogou? '))
for p in range(0, tot):
    partidas.append(int(input(f'   Quantos Gols na partida {p}? ')))
dados['total'] = (sum(partidas))
dados['gols'] = partidas[:]
print('-=' * 20)
print(f'o campo nome tem o valor {dados["nome"]}.')
print(f'o campo gols tem o valor {partidas}.')
print(f'o campo total tem o valor {dados["total"]}.')
print('-=' * 20)
print(f'o jogador {dados["nome"]} jogou {tot} partidas')
for i, v in enumerate(dados['gols']):
    print(f'  => Na partida {i}, fez {v} gols.')
print(f'foi um total de {dados["total"]} gols.')
