def tamanhodapalavra(t,p):                   #recebe duas palavras e checa qual delas é a maior
    if(len(t)>len(p)):
        print(f"A palavra {t} é maior que a palavra {p}")
    elif (len(t)<len(p)):
        print(f"A palavra {t} é menor que a palavra {p}")
    elif (len(t)==len(p)):
        print(f"A palavra {t} é igual a palavra {p}")
    else:
        print("Algo deu errado")
while(True):
    palavra1 =input("Insira a palavra 1:")
    palavra2 = input("Insira a palavra 2:")

    tamanhodapalavra(palavra1,palavra2)
    

