from rich import *
class Funcionarios:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    def apresentacao(self):
        return f':handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor {self.setor}'

c1 = Funcionarios('Max', 'TI', 'Programador')
print(c1.apresentacao())