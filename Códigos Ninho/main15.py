repetir = True
while (repetir):
    repetir = False

    num1 = (input('Digite o primeiro número:'))
    num2 = (input('Digite o segunto número:'))
    if (num1.isnumeric())and (num2.isnumeric()):
        num1 = float(num1)
        num2 = float(num2)

        operador = input('Digite a operação (+,-,*,/):')
        if (operador == "+" or operador.lower() == "soma"):
            print("A soma é:", num1+num2)

        elif (operador == "-" or operador.lower() == "subtração"): 
            print('A subtração é:', num1-num2)

        elif (operador == "/" or operador.lower() == "divisão"):
            if (num2 == 0):
                repetir = True
                print("Você tentou dividir por 0, operação inválida.")

            else:
                print("A divisão é:", num1/num2)

        elif (operador == "*" or operador.lower() == "multiplicação"):
            print("A multiplicação é:", num1*num2)
        else:
            print ("O operador que você digitou é inválido.")

    else:
        print("O operador que você digitou é inválido.")
        repetir = True

