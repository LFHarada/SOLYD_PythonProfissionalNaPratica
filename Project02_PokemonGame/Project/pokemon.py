import random


class Pokemon:

    def __init__(self, species, level=None, name=None):

        if species:
            self.species = species
        else:
            self.species = "Unknown"

        if name:
            self.name = name
        else:
            self.name = None

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 50)

        self.atk_pwr = self.level * 5
        self.life = self.level * 10

    def __str__(self):

        return "{} ({})".format(self.species, self.level)
        #if self.name:
        #    return "Name: {} \nSpecies: {} \nLevel: {}" \
        #        .format(self.name, self.species, self.level)
        #else:
        #    return "Species: {} \nLevel: {}" \
        #        .format(self.species, self.level)

    def atk(self, pokemon):

        effective_atk = int((self.atk_pwr * random.random() * 1.3))
        pokemon.life -= effective_atk

        print("{} lost {} health points.".format(pokemon, effective_atk))

        if pokemon.life <= 0:
            print("{} was defeated.".format(pokemon))
            return True
        else:
            return False


class PokemonGrass(Pokemon):
    type = "Grass"

    def atk_growl(self, pokemon):
        print("{} used Growl against {}".format(self, pokemon))
        return super().atk(pokemon)

    def atk_tackle(self, pokemon):
        print("{} used Tackle against {}".format(self, pokemon))
        return super().atk(pokemon)


class PokemonFire(Pokemon):
    type = "Fires"

    def atk_growl(self, pokemon):
        print("{} used Growl against {}".format(self, pokemon))
        return super().atk(pokemon)

    def atk_scratch(self, pokemon):
        print("{} used Scratch against {}".format(self, pokemon))
        return super().atk(pokemon)


class PokemonWater(Pokemon):
    type = "Water"

    def atk_tackle(self, pokemon):
        print("{} used Tackle against {}".format(self, pokemon))
        return super().atk(pokemon)

    def atk_tail_whip(self, pokemon):
        print("{} used Tail Whip against {}".format(self, pokemon))
        return super().atk(pokemon)


class PokemonElectric(Pokemon):
    type = "Electric"

    def atk_nuzzle(self, pokemon):
        print("{} used Nuzzle against {}".format(self, pokemon))
        return super().atk(pokemon)

    def atk_thunder_shock(self, pokemon):
        print("{} used Thunder Shock against {}".format(self, pokemon))
        return super().atk(pokemon)