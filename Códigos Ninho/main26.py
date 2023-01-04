def inteiro(n):                                                 # checar se o numero digitado é inteiro

    if (n.isnumeric()):
        print("Parabéns você escreveu um numero inteiro:")
        global repetir
        repetir = False
    else:
        print("Voce não escreveu um inteiro. Digite novamente:")


repetir = True
while (repetir):
    num= input("Digite um numero inteiro:")
    inteiro(num)