class Calculadora:
    def __init__(self):
        self.valor = ""

    def calcular(self,numero2,operador):
        try:
            numero2 = float()


        if(operador == "+"):
            print(self.somar(numero2))

        elif (operador == "-"):
            print(self.subtrair(numero2))

        elif(operador == "*"):
            print(self.multiplicar(numero2))

        elif (operador == "/"):
            print(self.dividir(numero2))
        
        else:
            print("O usuario digitou um operador inválido")    

    def somar(self,numero2):
        soma = self.valor + numero2
        self.valor = soma
        return soma 

    def subtrair(self,numero2):
        subtração = self.valor - numero2
        self.valor = subtração
        return subtração

    def multiplicar(self,numero2):
        multiplicaçao = self.valor * numero2
        self.valor = multiplicaçao
        return multiplicaçao

    def dividir(self,numero2):
        divisao = self.valor / numero2
        self.valor = divisao
        return divisao
    
calculadora = Calculadora()   

while (True):
    if (calculadora.valor == ""):
        calculadora.valor = int(input("Digite o numero 1:"))

    n2= int(input("Digite o numero 2:"))
    operador = input("Insira o operador:")

    calculadora.calcular(n2,operador)

