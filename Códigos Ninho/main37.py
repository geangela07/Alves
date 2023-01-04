#introcução a função classe

class Pokemon:                            
    def __init__(self,nome,tipo,especie,velocidade):
        self.nome = nome
        self.tipo = tipo
        self.especie = especie
        self.velocidade = velocidade

pokemon1 = Pokemon("Sperow","normal","pajarito","70")
print("Nome:",pokemon1.nome)
print("Tipo:",pokemon1.tipo)
print("Especie:",pokemon1.especie)
print("Velocidade:",pokemon1.velocidade)

pokemon2 = Pokemon("Cartepie","inseto","gusano","45")
print("Nome:",pokemon2.nome)
print("Tipo:",pokemon2.tipo)
print("Especie:",pokemon2.especie)
print("Velocidade:",pokemon2.velocidade)



