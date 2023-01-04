class Pokemon:
    def __init__(self,level,nome,hp,ataque):
        self.level = level
        self.nome = nome
        self.hp = hp
        self.ataque = ataque
        print("Pokemon criado")

    def atacar(self):
        print("O pokemon atacou")
    def checarVantagem(self,tipoInimigo):
        match tipoInimigo:
            case "Fogo":
                print(f"O pokemon{self.nome} perdeu para o {pokemonInimigo.tipo}")
            case "Agua":
                print(f"O pokemon{self.nome} perdeu para o {pokemonInimigo.tipo}")
            case "Eletrico":
                print(f"O pokemon {self.nome} perdeu para o {pokemonInimigo.tipo}")
            case "Grama":
                print(f"O pokemon {self.nome} perdeu para o {pokemonInimigo.tipo}")


    def PokemonAquatico(Pokemon):
        def __init__(self,level,nome,hp,ataque):
            super().__init__(level,nome,hp,ataque)
            self.level = level
            self.nome = nome
            self.hp = hp
            self.ataque = ataque
            print("Pokemon do tipo aquático criado")

        def atacar(self):
            print(f"O pokemon{self.nome}usou um jato d'agua para atacar")


    def PokemonFogo(Pokemon):
        def __init__(self,level,nome,hp,ataque):
            super().__init__(level,nome,hp,ataque)
            self.level = level
            self.nome = nome
            self.hp = hp
            self.ataque = ataque
            print("Pokemon do tipo fogo foi criado")

        


    def PokemonEletrico(Pokemon):
        def __init__(self,level,nome,hp,ataque):
            super().__init__(level,nome,hp,ataque)
            self.level = level
            self.nome = nome
            self.hp = hp
            self.ataque = ataque
            print("Pokemon do tipo eletrico foi criado")

        

        
if __name__ == "__main__":     # essa linha de codigo é usada para que essa parte do codigo não seja acessado em outro arquivo
    pokemon1 = Pokemon(10)
    pokemon2 = PokemonAquatico(15)

