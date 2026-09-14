import random

al1 = str(input('Primeiro Aluno: '))
al2 = str(input('Segundo Aluno: '))
al3 = str(input('Terceiro Aluno: '))
al4 = str(input('Quarto Aluno: '))
lista = [al1, al2, al3, al4]
random.shuffle(lista)
print(f'a ordem de apresentaçao sera \n{lista}')
