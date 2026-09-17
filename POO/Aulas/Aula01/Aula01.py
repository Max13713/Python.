class Pessoa:
    def __init__(self):
        self.nome = ''
        self.idade = 0
        self.altura = 0
    def anivesario(self):
        self.idade += 1
    def mesagem(self):
        return f'{self.nome} tem {self.idade} anos de idade.'

p1 = Pessoa()
p1.nome = 'Max'
p1.idade = 14
print(p1.mesagem())