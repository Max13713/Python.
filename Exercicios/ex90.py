aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno['nome']}: '))
if aluno['media'] >= 5:
    aluno['situaçao'] = 'aprovado'
elif aluno['media'] >= 5 and aluno['media'] <= 7:
    aluno['situaçao'] = 'recuperaçao'
else:
    aluno['situaçao'] = 'reprovado'
print('-=' * 20)
for k, v in aluno.items():
    print(f'  - {k} e igual a {v}')