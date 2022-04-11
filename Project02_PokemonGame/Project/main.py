import pickle

from person import *


def choose_first_pokemon(player):
    print("Hello {}, you can choose your initial pokemon now!".format(player))

    pikachu = PokemonElectric("Pikachu", level=1)
    charmander = PokemonFire("Charmander", level=1)
    squirtle = PokemonWater("Squirtle", level=1)

    print("You have 3 choices: ")
    print("1 -", pikachu)
    print("2 -", charmander)
    print("3 -", squirtle)

    while True:
        choice = input("Choose your Pokémon: ")

        if choice == "1":
            player.catch(pikachu)
            break
        elif choice == "2":
            player.catch(charmander)
            break
        elif choice == "3":
            player.catch(squirtle)
            break
        else:
            print("Invalid choice!")


def save_game(player):
    try:
        with open("database.db", "wb") as arquivo:
            pickle.dump(player, arquivo)
            print("Game saved!")
    except Exception as error:
        print("Error: Game could not be saved")
        print(error)


def load_game():
    try:
        with open("database.db", "rb") as arquivo:
            player = pickle.load(arquivo)
            print("Loading succeed!")
            return player
    except Exception as error:
        print("Save unreachable!")


if __name__ == "__main__":
    print('--------------------------------------------')
    print("Welcome to the Pokémon RPG: Terminal Edition")
    print('--------------------------------------------')

    player = load_game()

    if not player:
        nome = input("Hello, what is your name?: ")
        player = Player(nome)
        print("Hello {}, we divide this world with wonderful little creatures called Pokémon,"
              "your mission for now on is become a Pokemon Master Trainer!".format(player))
        print("Catch as many pokemons as you can and fight your enemies!")
        player.show_money()

        if player.pokemons:
            print("I already saw that you have some pokemons!")
            player.show_pokemons()
        else:
            print("You don't have any pokemon, so you need to choose one!")
            choose_first_pokemon(player)

        print("Alright, now that you have your Pokémon, you must confront your arch-rival, Gary.")
        gary = Enemy(full_name="Gary", pokemons=[PokemonWater("Squirtle", level=1)])
        player.battle(gary)
        save_game(player)

    while True:
        print("--------------------------------------")
        print("MENU")
        print("1 - Explore")
        print("2 - Fight an enemy")
        print("3 - Pokedex")
        print("0 - Exit game")
        escolha = input("Choice (number): ")

        if escolha == "0":
            print("Closing game...")
            break
        elif escolha == "1":
            player.explore()
            save_game(player)
        elif escolha == "2":
            inimigo_aleatorio = Enemy()
            player.battle(inimigo_aleatorio)
            save_game(player)
        elif escolha == "3":
            player.show_pokemons()
        else:
            print("Invalid choice")