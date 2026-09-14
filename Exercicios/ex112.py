from mex112.utilidadescev import dados
from mex112.utilidadescev import moeda

preço = dados.leiadinheiro('Digite o preço: R$')
moeda.resumo(preço, 35, 22)