unidades = ("unidade","centena","dezena","milhar")
numeroInvertido = []

while (True):
    numero = input("Digite um numero de até 4 digitos:")
    if (numero.isnumeric()):
        if(len(numero)<= 4):
            for i in range(len(numero)):
        else:
            print("Voce deve escrever um número de até 4 digitos")
    else:
        print("Voce digitou um caractere que não é um numero")