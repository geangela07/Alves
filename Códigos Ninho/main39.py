# o proggrama recebe o valor do salario e imprimi o salario atual e o salario depois do aumento

class Funcionario:                                     
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario
    def aumentarSalario(self,percentualdeAumento):
        self.salario = self.salario * (1+percentualdeAumento/100)

funcionario1 = Funcionario("José",3000)

print(f"Salario atual:{funcionario1.salario}")
funcionario1.aumentarSalario(20)

print(f"Salario depois do aumneto:{funcionario1.salario}")
        
        