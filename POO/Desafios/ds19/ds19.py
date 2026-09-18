from rich import print
from time import sleep
class Livro:
    def __init__(self, titulo ,paginas):
        self.titulo = titulo
        self.total_de_paginas = paginas
        self.pagina_atual = 1
        print(f':: [blue]Vc acabou de abrir o livro "[red]{self.titulo}[/]" que tem [green]{self.total_de_paginas} Paginas[/] no total. Vc esta agora na [yellow]pagina 1[/][/]')
    def avançar_paginas(self, qtd=1):
        cont = 0
        for p in range(0, qtd, 1):
            if not self.fim_do_livro():
                sleep(.2)
                self.pagina_atual += 1
                print(f'Pág{self.pagina_atual} :arrow_forward:', end=' ')
                cont += 1
        print(f'[blue]Voce avançou {cont} paginas e agora esta na [yellow]pagina {self.pagina_atual}[/][/]')
        if self.fim_do_livro():
            print(f'[red]:closed_book: Vc chegou ao final do livro [/]{self.titulo}')

    def fim_do_livro(self):
        return True if self.pagina_atual >= self.total_de_paginas else False

l1 = Livro('Logica de programaçao para leigos',20)
l1.fim_do_livro()
l1.avançar_paginas(5)
l1.avançar_paginas(10)
l1.avançar_paginas(50)
l1.avançar_paginas(5)