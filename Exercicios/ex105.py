def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
        :param n: uma ou mais notas dos alunos (aceita várias)
        :param sit: valor opcional, indicando se deve ou não adicionar a situação
        :return: diclionário com várias informações sobre a situação da turma.
    """
    notas = dict()
    notas['total'] = len(n) 
    notas['maior'] = max(n)
    notas['menor'] = min(n)
    notas['media'] = sum(n) / len(n)
    if sit:
        if notas['media'] >= 7:
            notas['situaçao'] = 'BOA'
        elif notas['media'] <= 7 and notas['media'] >= 5:
            notas['situaçao'] = 'RAZOAVEL'
        else:
            notas['situaçao'] = 'RUIM'
    return notas
resp = notas(3.4, 10, 6.5, sit=True)
print(resp)
help(notas)