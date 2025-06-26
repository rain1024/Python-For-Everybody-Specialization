# Define a "class" to create Pokemon objects
class Pokemon:
    # Constructor method (__init__) to set up initial attributes
    def __init__(self, name, pokemon_type, hp, level):
        # These are ATTRIBUTES (attributes or fields)
        # They store data and state of the object
        self.name = name
        self.pokemon_type = pokemon_type
        self.hp = hp
        self.level = level
        print(f"Created a Pokemon named {self.name}!")

    # This is a METHOD
    # It defines an action that the object can perform
    def attack(self, other_pokemon):
        print(f"{self.name} attacks {other_pokemon.name}!")
        # (Add damage logic here)

# Create a specific OBJECT from the Pokemon class
pikachu = Pokemon("Pikachu", "Electric", 100, 5)

# Access the ATTRIBUTE (attribute/field) of the pikachu object
print(f"Pokemon's name is: {pikachu.name}")
print(f"Its type is: {pikachu.pokemon_type}")

# Create another object
charmander = Pokemon("Charmander", "Fire", 95, 5)

# Call the METHOD of the pikachu object
pikachu.attack(charmander)