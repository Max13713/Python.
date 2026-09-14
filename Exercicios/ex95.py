jogadores = list()
dados = dict()
while True:
    partidas = list()
    dados['nome'] = str(input('Nome do Jogador: '))
    dados['total'] = int(input(f'Quantas Partidas {dados['nome'].capitalize()} jogou? '))
    for p in range(0, dados['total']):
        partidas.append(int(input(f'   Quantos Gols na partida {p}? ')))
    dados['total'] = (sum(partidas))
    dados['gols'] = partidas[:]
    jogadores.append(dados.copy())
    while True:
        cont = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
        if cont in 'SN':
            break
        print('ERRO! por favor, digite apenas S ou N')
    if cont == 'N':
        break
print('-' * 40)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(jogadores):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    elif busca >= len(jogadores):
         print(f'  - ERRO! Nao existe jogador com codigo {busca}! Tente Novamente')
    else:
        print(f' -- Levantamente do Jogador {jogadores[busca]['nome']}:')
        for i, g in enumerate(jogadores[busca['gols']]):
            print(f' => No jogo {p}, fez {g} gols.')
print('-=' * 20)