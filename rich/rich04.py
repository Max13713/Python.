from rich import inspect

class ContaBancaria:
    """
    cria uma conta bancaria e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo=0 ):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'conta {self.id} criada com sucesso. saldo atual de R${self.saldo:,.2f}')

    def __str__(self) -> str:
        return f'a conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo'

    def deposito(self, valor):
        self.saldo += valor
        print(f'Deposito de R${valor:,.2f} autorizado na conta {self.id}')

    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saque NEGADO de R${valor:,.2f} na conta {self.id} SALDO INSUFICIENTE')
        else:
            self.saldo -= valor
            print(f'Saque de R${valor:,.2f} autorizado na conta {self.id}')
conta1 = ContaBancaria(140371033, 'Max', 1000)
conta1.deposito(1500)
print(conta1.saldo)

inspect(conta1)

while True:
    try:
        conta1.sacar(float(input('Quanto vc quer sacar? ')))
    except:
        print('Erro!')
    print(conta1)

