Nome =(input('Digite um nome:'))
A = float(input('Digite a nota A:'))
B =float(input('Digite a nota B:'))
C =float(input('Digite a nota C:'))
media= (A+B+C)/3
if (media>=7):
    print('Aprovado')
elif (media <=5):
    print ('Reprovado')
elif (media >= 5.1 and media <= 6.9):
    print ('Recuperação')
else:
    print('Notas invalidas')
