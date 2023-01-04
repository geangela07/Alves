def potencia(a,b):
    resultado = 1
    for numero in range (b):
        resultado = resultado * b
        return resultado

base = input("Digite o numero a:")
expoente = input("Digite o numero b:")

print(potencia(int(base),int(expoente)))



