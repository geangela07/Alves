def checarletra(l,p):                                #checar se a letra existe na palavra
    if(l in p):
        print(f"A letra {l} existe na palavra {p} ")
    else:
        print(f"A letra {l} não existe na palavra {p}")
checarletra("t","teste")

checarletra("k","tela")