class Triangulo:                                  #o programa recebe os lados de um triangulo e calcula seu perimetro e o seu maior lado
    def __init__(self,LadoA,LadoB,LadoC):
        self.LadoA = LadoA
        self.LadoB = LadoB
        self.LadoC = LadoC
        self.maiorLado = ""

    def calcularPerimetro(self):
        perimetro = float(self.LadoA) + float(self.LadoB) + float(self.LadoC)
        return perimetro

    def getMaiorlado(self):

        if (self.LadoA >= self.LadoB and self.LadoA >= self.LadoC):
            self.maiorLado = self.LadoA
        elif(self.LadoB >= self.LadoA and self.LadoB >= self.LadoC):
            self.maiorLado = self.LadoB
        elif(self.LadoC >= self.LadoA and self.LadoC >= self.LadoB):
            self.maiorLado = self.LadoC
        else:
            self.maiorLado = "Alguns lados sao iguais"


Triangulo1 = Triangulo("7","8","9")
print(Triangulo1.calcularperimetro())
Triangulo1.getMaiorlado()
print(Triangulo1.maiorLado)

        