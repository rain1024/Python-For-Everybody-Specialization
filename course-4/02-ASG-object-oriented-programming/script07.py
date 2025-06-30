# --- PARENT CLASS ---
class Animal:
    def __init__(self, name):
        self.name = name

    # All animals have this behavior
    def eat(self):
        print(f"{self.name} is eating...")

    # A common behavior that may be redefined by child classes
    def make_sound(self):
        print(f"{self.name} makes some sound...")

# --- CHILD CLASS ---
# Dog class inherits from Animal class
# Note the syntax: class Dog(Animal):
class Dog(Animal):
    # Dog class doesn't need to redefine __init__ or eat()
    # because they are "inherited" for free from Animal.

    # Redefine (override) the make_sound() method from parent class
    def make_sound(self):
        print(f"{self.name} says: Woof woof!")

# Another child class, also inherits from Animal
class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says: Meow meow!")

# --- CREATE OBJECTS ---
print("--- Creating Dog object ---")
golden = Dog("Golden")
golden.eat()      # Call method inherited from Animal
golden.make_sound()  # Call method redefined in Dog class

print("\n--- Creating Cat object ---")
munchkin = Cat("Munchkin")
munchkin.eat()    # Also inherits the eat() method
munchkin.make_sound()  # Call method redefined in Cat class