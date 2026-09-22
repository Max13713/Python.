from rich import print
class Caneta:
    def __init__(self, cor='azul'):
        escolha = ''
        match cor.lower().strip():
            case 'azul':
                escolha = '[blue]'
            case 'vermelho':
                escolha = '[red]'
            case 'verde':
                escolha = '[green]'
            case _:
                escolha = '[while]'
        self.cor = escolha
        self.tampada = True

    def quebra_linha(self, qtd=1):
        print('\n' * qtd, end='')

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False

    def escrever(self, text):
        if self.tampada:
            print(f':no_entry_sign: A {self.cor}caneta[/] esta tampada!')
        else:
            print(f'{self.cor}{text}[/]', end='')
c1 = Caneta()
c1.destampar()
c1.escrever('teste 1')
c1.quebra_linha(2)
c1.escrever('teste 2')
c1.escrever('teste 3')