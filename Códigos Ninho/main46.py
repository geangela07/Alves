import random

especiesPokemon = ("Pikachu","Charmander","Cartepie")

meuPokemon = especiesPokemon[random.randint(0,len(especiesPokemon)-1)]

match meuPokemon:
    case "Pikachu":
        meuPokemonAtaque = random.randint(30,50)
        meuPokemonDefesa = random.randint(30,50)
        meuPokemonHp = random.randint(30,50)

    case "Charmander":
        meuPokemonAtaque = random.randint(50,60)
        meuPokemonDefesa = random.randint(50,60)
        meuPokemonHp = random.randint(50,60)

    case "Cartepie":
        meuPokemonAtaque = random.randint(20,30)
        meuPokemonDefesa = random.randint(20,30)
        meuPokemonHp = random.randint(20,30)



pokemonInimigo = random.choice(especiesPokemon)

match pokemonInimigo:
    case "Pikachu":
        pokemonInimigoAtaque = random.randint(30,50)
        pokemonInimigoDefesa = random.randint(30,50)
        pokemonInimigoHp = random.randint(30,50)

    case "Charmander":
        pokemonInimigoAtaque = random.randint(50,60)
        pokemonInimigoDefesa = random.randint(50,60)
        pokemonInimigoHp = random.randint(50,60)

    case "Cartepie":
        pokemonInimigoAtaque = random.randint(20,30)
        pokemonInimigonDefesa = random.randint(20,30)
        pokemonInimigoHp = random.randint(20,30)

forçameuPokemon = meuPokemonAtaque + meuPokemonDefesa + meuPokemonHp
forçapokemonInimigo = pokemonInimigoAtaque +pokemonInimigoDefesa + pokemonInimigoHp

print("Meu Pokemon:",meuPokemon,meuPokemonAtaque,meuPokemonDefesa,meuPokemonHp)
print("Pokemon Inimigo:",pokemonInimigo,pokemonInimigoAtaque,pokemonInimigoDefesa,pokemonInimigoHp)

if forçameuPokemon > forçapokemonInimigo:
    print("Eu ganhei")

elif forçameuPokemon < forçapokemonInimigo:
    print("Eu perdi")

else:
    print("Deu empate")

        

        