def checarletra(p,l):                #checar a quantidade de letras exite na palavra
    contador = 0
    for i in range(len(p)):
        if (p[i]== l):
            contador += 1
    return contador

palavra = input("Esceva a palavra:")
letra = input ("Escreva a letra para verificar:")
print (checarletra(palavra.lower(),letra.lower()))
