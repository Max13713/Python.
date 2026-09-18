from rich import print
from rich.panel import Panel
class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = list([])
    def add_favoritos(self, jogo):
        self.jogos_favoritos.append(jogo)
        self.jogos_favoritos = sorted(self.jogos_favoritos)
    def ficha(self):
        conteudo = f'Nome real: {self.nick}'
        conteudo += f'\nJogos favoritos: '
        for jogo in self.jogos_favoritos:
            conteudo += f'\n:: [blue]{jogo}[/]'
        ficha = Panel(conteudo, title=f'Jogador <{self.nick}>', width=35)
        print(ficha)
j1 = Gamer('Paulo', 'Max137')
j1.add_favoritos('Fortnite')
j1.add_favoritos('Red Dead Remdeption 2')
j1.add_favoritos('Resident evil 4')
j1.add_favoritos('Minecraft')
j1.add_favoritos('Dredge')
j1.ficha()
