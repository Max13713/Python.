nome= str(input('Nome completo:')).strip()
n = len(nome.split()) - 1
print(f'primeiro {nome.split()[0]}')
print(f'ultimo {nome.split()[n]}')
