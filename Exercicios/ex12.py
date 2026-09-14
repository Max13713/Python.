produto = float(input('Qual o preço do produto?: ')) 
#ValorDesconto = int(input('Quantos porcento de desconto vc quer colocar?: '))
desconto = (produto * 5) / 100
valorFinal = produto - desconto
print(f'o preço final depois do desconto e de {valorFinal:.2f}')

