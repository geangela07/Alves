notas = []
maior = []
while(len(notas)< 5):
    notas.append(float(input("Digite a nota:")))

soma = sum(notas)
media = soma /len(notas)

print("A soma das nota é:",soma)
print("A media das notas é:",media)

for i in notas:
    if (i > media):
        maior.append(i)

print(f"Os valores maiores que a media são:{maior}")



         
