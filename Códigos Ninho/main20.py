
# Calculadora

def soma(numero1,numero2):
    return float(numero1) + float(numero2)

def subtração(numero1,numero2):
    return float(numero1) - float(numero2)

def multiplicação(numero1,numero2):
    return float(numero1) * float(numero2) 

def divisão (numero1,numero2):
    if (num2 == 0):
        return ("O num2 não pode ser 0.")

    
    return float(numero1) / float(numero2)

def calculadora(n1,n2,op):
    if (op == "+"):
        print(soma(n1,n2))

    elif (op == "-"):
        print(subtração(n1,n2))

    elif (op == "*"):
        print(multiplicação(n1,n2))

    elif (op == "/"):
        print(divisão(n1,n2))
    else:
        print("O usuario digitou um operador inválido.")
    global repetir
    repetir = True


repetir = True
while (repetir == True):

    num1 = input("Escreva o número 1:")
    num2 = input("Escreva o número 2:")
    operador = input("Escreva o operador (+,-,*,/)")

    if (num1.isnumeric() and num2.isnumeric()):
        repetir = False
        calculadora(num1,num2,operador)
    else:
        repetir = True
        print("O usuario digitou um numero invalido.")
        









