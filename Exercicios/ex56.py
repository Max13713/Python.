nome = str
idade = int
sexo = str
listaM = []
listaIM = []
contagem = 0
for c in range(0, 4):
    print(f'----- {c} PESSOA -----')
    nome = str(input('Nome: ')).upper().strip()
    idade = int(input('Idade: '))
    sexo = str(input('sexo [M/F]: ')).upper().strip()
    if  sexo == 'M':
        listaIM.append(nome)
        listaM.append(idade)
    elif sexo == 'F':
        if idade < 20:
            contagem += 1
media = sum(listaM) / len(listaM)
maism = listaIM[(listaM.index(max(listaM)))]
print(f'a media de idade do grupo e {media}')
print(f'o homen mais velho tem {max(listaM)} anos e se chama {maism}')
print(f'ao todo sao {contagem} {'mulher' if contagem < 2 else 'mulheres'} com menos de 20 anos') if contagem == 0 else print('nao tem nenhuma mulher com menos de 20 anos')
