class Livros:
    def __init__(self, nome,qtdpaginas,autor,preco):
        self.nome = nome
        self.qtdpaginas = qtdpaginas
        self.autor = autor
        self.preco = preco
    
    def getPreco(self):
        return self.preco

    def setPreco(self,novoPreco):
        self.preco = float(novoPreco)

livro1 = ("Jaguar",100,"Jorge",25)
print(livro1.getPreco())
livro1.setpreco()
print(livro1.getpreco())