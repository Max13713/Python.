from mex115.lib.interface import *
from mex115.lib.arquivo import *
from time import sleep

arq = 'Ex115Dados.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['\033[34mVer pessoas cadastradas\033[m', '\033[34mCadastra nova pessoa\033[m', '\033[34mSair do sistema\033[m'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        sair()
        break
    else:
        print('\033[31mERRO! Digite uma opçao valida!.\033[m')
    sleep(2)