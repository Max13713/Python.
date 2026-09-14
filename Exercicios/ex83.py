exprer = (input('digite a expreçao: '))
pilha = list()
for s in exprer:
    if s == '(':
        pilha.append('(')
    else:
        if s == ')':
            if len(pilha) > 0:
                pilha.pop()
            else:
                pilha.append(')')
                break
if len(pilha) == 0:
    print('sua expreçao esta valida!')
else:
    print('sua expreçao esta errada!')