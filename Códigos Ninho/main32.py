
numero = input("Digite o numero:")
if numero.isnumeric():
     if len(numero) >= 4:
            numero = int(numero)
            m = numero//1000
            c = (numero - (1000*m)) //100
            d = (numero -(100*c)) - (1000*m)//10
            u = (numero - (10*d) - (100*c) - (1000*m))
print (f""" 
    Milhares:{m}
    Centenas: {c}
    Dezenas: {d}
    Unidades: {u}
    """)
