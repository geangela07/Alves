while True:                     #receber apenas senha numerica
    senha = input("Crie uma a senha:")
    list(senha)
    if len(senha) < 4:
        print(" A senha deve ter no minimo 4 numeros.")
    elif len(senha) > 8:
        print ("A senha deve ter no máximo 8 numeros. ")
    else:
        if any(x.isnumeric() == False for x in senha):
            print("Deve conter só numeros")
        else:
            break
print("Senha válida")

