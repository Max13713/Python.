frase = str(input('Digite uma frase: ')).strip().lower()
print(f'a letra A parece {frase.count('a')} vezes na frase')
print(f'a letra A aparece pela primeira vez na posiçao {frase.find('a')+1}')
print(f'a letra A aparece pela ultima vez na posiçao {frase.rfind('a')+1}')