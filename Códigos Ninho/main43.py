

maior = 0
while (True):
    n = int(input("Digite um numero:"))


    if (n > maior):
        maior = n


    if (n == 0):
        break
print("O maior numero é",maior)


for i in range(1,101):
    if(i % 10):
        print (f"O número {i} é múltiplo de 10")