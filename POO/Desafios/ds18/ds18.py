from rich.panel import Panel
from rich import print
class Churrasco:

    consumo_padrao: float = 0.400
    preco_kg: float = 82.40

    def __init__(self, titulo, quant):
        self.quantidadePessoas = quant
        self.titulo = titulo

    def calcular_qtd_carne(self) -> float:
        return Churrasco.consumo_padrao * self.quantidadePessoas

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * Churrasco.preco_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.quantidadePessoas

    def analisar(self):
        conteudo = f'Analisando [green]{self.titulo}[/] com [blue]{self.quantidadePessoas} convidados[/]'
        conteudo += f'\nCada participante comera {Churrasco.consumo_padrao}Kg e cada Kg custa R${Churrasco.preco_kg}'
        conteudo += f'\nRecomendo [blue]comprar {self.calcular_qtd_carne():.3f}Kg[/] de carne'
        conteudo += f'\nO custo total sera de [green]R${self.calcular_custo_total():,.2f}[/]'
        conteudo += f'\nCada pessoa pagara [yellow]R${self.calcular_custo_individual():,.2f}[/]'
        painel = Panel(conteudo, title=self.titulo)
        print(painel)
churras1 = Churrasco('Churras Dos Amigos', 100)
churras1.analisar()