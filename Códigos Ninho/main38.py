#desativar uma pessoa da lista

class Pessoa:
    def __init__(self,nome,sexo,cpf,ativo):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.ativo = ativo

    def desativar(self):
        self.ativo = False
        print("A pessoa {self.nome}foi desativada com sucesso")

pessoa1 =Pessoa("Joana","F","96325874114",True)
pessoa1.desativar()

if (pessoa1.ativo == True):
    print("A pessao{pessoa1.nome}está ativo")
else:
    print("A pessoa{pessoa1.nome} não está ativo")