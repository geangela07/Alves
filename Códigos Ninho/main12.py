palavra = input('Escreva uma palavra:')

palavraInvertida = ""

for i in range(len(palavra)):
    palavraInvertida += palavra[(len(palavra)-1)-i]
    print(palavraInvertida)