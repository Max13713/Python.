def ficha(nome='<desconhecido>', gols=0):
    print(f'o jogador {nome} fez {gols} gol(s) no campeonado.')
nome = str(input('Nome do jogador: '))
gols = str(input('Numero de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome, gols)
