from pokemon import *

FIRSTNAMES = [
    "Miguel", "Davi", "Arthur", "Pedro", "Gabriel", "Bernardo", "Lucas", "Matheus", "Rafael", "Heitor", "Enzo",
    "Guilherme", "Nicolas", "Lorenzo", "Gustavo", "Felipe", "Samuel", "João Pedro", "Daniel", "Vitor", "Leonardo",
    "Henrique", "Theo", "Murilo", "Eduardo", "Pedro Henrique", "Pietro", "Cauã", "Isaac", "Caio", "Vinicius",
    "Benjamin", "João", "Lucca", "João Miguel", "Bryan", "Joaquim", "João Vitor", "Thiago", "Antônio", "Davi Lucas",
    "Francisco", "Enzo Gabriel", "Bruno", "Emanuel", "João Gabriel", "Ian", "Davi Luiz", "Rodrigo", "Otávio",
    "Sophia", "Alice", "Julia", "Isabella", "Manuela", "Laura", "Luiza", "Valentina", "Giovanna", "Maria Eduarda",
    "Helena", "Beatriz", "Maria Luiza", "Lara", "Mariana", "Nicole", "Rafaela", "Heloísa", "Isadora", "Lívia",
    "Maria Clara", "Ana Clara", "Lorena", "Gabriela", "Yasmin", "Isabelly", "Sarah", "Ana Julia", "Letícia",
    "Ana Luiza", "Melissa", "Marina", "Clara", "Cecília", "Esther", "Emanuelly", "Rebeca", "Ana Beatriz", "Lavínia",
    "Vitória", "Bianca", "Catarina", "Larissa", "Maria Fernanda", "Fernanda", "Amanda", "Alícia", "Carolina", "Agatha",
    "Gabrielly"
]

LASTNAMES = [
    "Silva", "Santos", "Pereira", "Ferreira", "Costa", "Oliveira", "Rodrigues", "Martins", "Fernandes", "Sousa",
    "Gonçalves", "Gomes", "Lopes", "Carvalho", "Ribeiro", "Pinto", "Marques", "Almeida", "Alves", "Teixeira", "Dias",
    "Monteiro", "Correia", "Boreira", "Mendes", "Vieira", "Cardoso", "Soares", "Nunes", "Rocha", "Barbosa",
    "Nascimento", "Machado", "Melo", "Castro", "Moura", "Jesus", "Abreu", "Aguiar", "Azevedo", "Campos", "Cunha",
    "Domingues", "Fonseca", "Freitas", "Miranda", "Ramos", "Reis", "Lima", "Andrade"
]

POKEMONS = [
    PokemonFire("Charmander"), PokemonFire("Charmeleon"), PokemonFire("Charzirard"),
    PokemonGrass("Bulbasaur"), PokemonGrass("Ivysaur"), PokemonGrass("Venusaur"),
    PokemonWater("Squirtle"), PokemonWater("Wartortle"), PokemonWater("Blastoise"), PokemonWater("Magikarp"),
    PokemonElectric("Pikachu"), PokemonElectric("Raichu")
]


class Person:

    def __init__(self, full_name=None, pokemons=[], dinheiro=random.randint(1, 10000)):

        self.first_name = random.choice(FIRSTNAMES)
        self.middle_name = random.choice(LASTNAMES)
        self.last_name = random.choice(LASTNAMES)
        self.pokemons = pokemons
        self.money = dinheiro
        if full_name:
            self.full_name = full_name
        else:
            self.full_name = self.first_name + self.middle_name + self.last_name

    def __str__(self):

        return self.full_name

    def show_pokemons(self):
        if self.pokemons:
            print("{}'s Pokemons:".format(self))
            for index, pokemon in enumerate(self.pokemons):
                print("{} - {}".format(index, pokemon))
        else:
            print("{} don't have any pokemon.".format(self))

    def choose_pokemon(self):
        if self.pokemons:
            pokemon_choice = random.choice(self.pokemons)
            print("{} choose {}".format(self, pokemon_choice))
            return pokemon_choice
        else:
            print("ERROR: This player have no pokemons.")

    def show_money(self):
        print("You have $ {} in your bank account.".format(self.money))

    def earn_money(self, quantity):
        self.money += quantity
        print("You received $ {}".format(quantity))
        self.show_money()

    def battle(self, person):
        print("{} started a battle with {}".format(self, person))
        person.show_pokemons()
        enemy_pokemon = person.choose_pokemon()
        pokemon = self.choose_pokemon()
        if pokemon and enemy_pokemon:
            while True:
                victory = pokemon.atk(enemy_pokemon)
                defeat = enemy_pokemon.atk(pokemon)

                if victory:
                    print("{} won the battle!".format(self))
                    self.earn_money(enemy_pokemon.level * 100)
                    break
                if defeat:
                    print("{} won the battle!".format(person))
                    break
        else:
            print("Essa batalha não pode ocorrer")


class Player(Person):

    tipo = "Player"

    def catch(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} captured {}!".format(self, pokemon))
        print("Gotcha!")

    def choose_pokemon(self):

        self.show_pokemons()

        if self.pokemons:
            while True:
                choice = input("Choose your Pokémon: ")
                try:
                    escolha = int(choice)
                    pokemon_escolhido = self.pokemons[escolha]
                    print("{}, i choose you!!!".format(pokemon_escolhido))
                    return pokemon_escolhido
                except:
                    print("Invalid choice.")
        else:
            print("ERROR: This player does not have any pokemon.")

    def explore(self):

        if random.random() <= 0.3:
            pokemon = random.choice(POKEMONS)
            print("An wild {} appeared!".format(pokemon))
            choice = input("Catch? (y or yes/n or no): ")

            if choice == "y" or "yes":
                if random.random() >= 0.5:
                    self.catch(pokemon)
                else:
                    print("Wild {} fled!".format(pokemon))
            else:
                print("Okay, good travel.")
        else:
            print("This exploration was not successful.")


class Enemy(Person):

    type = "Enemy"

    def __init__(self, full_name=None, pokemons=None):
        if not pokemons:
            random_pokemon = []
            for i in range(random.randint(1, 6)):
                random_pokemon.append(random.choice(POKEMONS))
            super().__init__(full_name=full_name, pokemons=random_pokemon)
        else:
            super().__init__(full_name=full_name, pokemons=pokemons)


class NonPlayer(Person):

    type = "Non Player Character"