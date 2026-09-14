from time import sleep
emp = float(input('valor da casa: R$'))
salario = float(input('salario do comprador: R$'))
anos = int(input('quantos anos de finaciamento? '))
print('Processando...')
sleep(2)
prestaçao = emp / (anos * 12)
minimo = (salario * 30 / 100)
if prestaçao <= minimo:
    print(f'para pagar uma casa de R${emp:.2f} em {anos} anos a prestaçao sera de R${prestaçao:.2f}')
    print('emprestimo aprovado')
else:
    print(f'Para pagar uma casa de R${emp:.2f} em {anos} anos a prestaçao sera de R${prestaçao:.2f}')
    print('emprestimo negado')
