# Alves
def gorjeta_garçom(valordaconta):
    print("O valor da gorjeta é:",valordaconta*10/100)

valor= float (input("Digite o valor da conta:"))

if (valor.isnumeric()):
    gorjeta_garçom(float(valor))
else:
    print("O usuario não digitou número")
