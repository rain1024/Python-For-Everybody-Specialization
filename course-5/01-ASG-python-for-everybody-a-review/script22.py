print("=== Demonstration of self, class and object ===")

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

animal1 = Animal("Animal 1")
print(animal1)
