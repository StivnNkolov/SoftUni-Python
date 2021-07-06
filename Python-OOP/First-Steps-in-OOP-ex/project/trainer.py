from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        for poke in self.pokemons:
            if pokemon_name == poke.name:
                self.pokemons.remove(poke)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        # print(f"Pokemon Trainer {self.name}")
        # print(f"Pokemon count {len(self.pokemons)}")
        # details = ''
        # for el in self.pokemons:
        #     details += f"- {el.pokemon_details()}\n"
        return f"""Pokemon Trainer {self.name}
Pokemon count {len(self.pokemons)}
- {' '.join([el.pokemon_details() for el in self.pokemons])}"""


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))

print(trainer.trainer_data())
