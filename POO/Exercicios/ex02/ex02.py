class Pessoa:
    """
    Essa classe cria uma Pessoa, que é uma pessoa que tem nome e idade.
    para criar uma nova pessoa, use
    variavel = Pessoa(nome, idade)
    """
    def __init__(self, nome='vazio', idade=0):
        self.nome = nome
        self.idade = idade
    def anivesario(self):
        self.idade += 1
    def __str__(self):
        return f'{self.nome} tem {self.idade} anos de idade.'
    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"
p1 = Pessoa('Max', 14)
p1.anivesario()
print(p1)
print(p1.__dict__)
print(p1.__getstate__())
print(p1.__class__)
