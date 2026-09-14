nota1 = float(input('primeira nota: '))
nota2 = float(input('segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'Tirando {nota1:.1f} e {nota2:.1f}, a media do aluno e {media:.1f}.')
    print('o aluno esta reprovado.')
elif media > 5 and media < 5.9:
    print(f'Tirando {nota1:.1f} e {nota2:.1f}, a media do aluno e {media:.1f}.')
    print('o aluno esta em:.1f recuperaç:.1fao.')
else:
    print(f'Tirando {nota1:.1f} e {nota2:.1f}, a media do aluno e {media:.1f}.')
    print('o aluno esta aprovado.')