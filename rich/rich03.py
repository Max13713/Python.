from rich import print, table
from rich.table import Table

tabela = Table(title='tabela de preços')

tabela.add_column('nome', justify='center')
tabela.add_column('idade', justify='center')

tabela.add_row('max', '14')

print(tabela)
