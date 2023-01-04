def soma(num1,num2):                                # Calculadora 
    return float (num1) + float (num2)

def subtração(num1,num2):
    return float (num1) - float (num2)

def multiplicação(num1,num2):
    return float(num1) * (num2)

def divisão(num1,num2):
    if (num2 == "0"):
        global repetir
        repetir = True
        return ("O número 2 não pode ser 0")
    else:
        return float (num1) / float(num2)

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
        
