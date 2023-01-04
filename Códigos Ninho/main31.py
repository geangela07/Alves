def verificarsenha(senha):               # receber uma senha que tenha entre 4 e 8 digitos e somente numeros
    
    if (senha.isnumeric()):
        if(len(senha)>= 4 and len(senha)<= 8 ):
            print("Sua senha é válida")
            global repetir
            repetir = False

        else:
            print(f"Sua senha tem {len(senha)}digitos.Digite uma senha entre 4 e 8 digitos")
    else:
        print("Você digitou uma senha numeros e letras")
repetir = True
while repetir:
    s = input("Digite a senha:")
    verificarsenha(s)

            
