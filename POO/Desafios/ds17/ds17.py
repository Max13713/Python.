from rich import print
from rich.panel import Panel
class Produto:
    def __init__(self, nome='Vazio', preco=0):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        conteudo = f'{self.nome.center(30, ' ')}'
        conteudo += f'{'-' * 30}'
        precof = f'R${self.preco:,.2f}'
        conteudo += f'{precof.center(30, '.')}'
        etiqueta = Panel(conteudo,title='Produto', width=35)
        print(etiqueta)
p1 = Produto('Pc', 2500)
p2 = Produto('Garrafa', 39.90)
p1.etiqueta()
p2.etiqueta()