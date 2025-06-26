# --- CLASS: DEFINING "PARTY ANIMAL" SPECIES ---
# This is the design template
class PartyAnimal:
    # Constructor function, called when a new PartyAnimal is created
    def __init__(self, name):
        self.name = name
        self.points = 0
        print(f"{self.name} has been created, ready to party!")

    # A method (behavior)
    def party(self):
        self.points = self.points + 1
        print(f"{self.name} has joined the party, fun points are now {self.points}")


# --- OBJECT INSTANTIATION ---

# This line uses the "template" PartyAnimal to create a new object
# and assigns it to the variable 'zap'.
print("--- Creating zap ---")
zap = PartyAnimal("Zappy")

# Create another object, also from the PartyAnimal template
# to show that each object is independent
print("\n--- Creating zoe ---")
zoe = PartyAnimal("Zoe")

# We have two different objects created from the SAME class
print(f"\nVariable zap points to object: {zap}")
print(f"Variable zoe points to object: {zoe}")

# Since they are separate objects, actions of one object don't affect the other
print("\n--- Let the party begin! ---")
zap.party()  # Zappy's points increase by 1
zoe.party()  # Zoe's points increase by 1
zap.party()  # Zappy's points increase by 2
