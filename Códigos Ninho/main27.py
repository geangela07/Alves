def f5(a):                               #Verificar a diferença entre variavel global e variavel local
    a=[10,10]
    a.append(3)
    print("Dentro da função",a)

a =[1,2]
f5(a)
print("Fora da função",a)
