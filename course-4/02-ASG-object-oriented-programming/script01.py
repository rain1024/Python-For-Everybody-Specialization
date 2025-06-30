# Step 1: Create "blueprint" or "template"
# We define a Class named Dog
class Dog:
    # This is the constructor method, it runs every time a new object is created
    def __init__(self, name, breed):
        # Attributes of each dog
        self.name = name
        self.breed = breed
        print(f"A new dog named {self.name} has been created!")

    # Method - behavior of the dog
    def bark(self):
        return f"{self.name} is barking: Woof! Woof!"

# --- Must have Class above before doing the step below ---

# Step 2: Create "concrete objects" from the blueprint
# We create Instances from the Dog class
my_dog_1 = Dog("Lu", "German Shepherd")
my_dog_2 = Dog("Max", "Golden Retriever")

# Now we have 2 separate dog objects
print(f"The name of the first dog is: {my_dog_1.name}")
print(f"The breed of the second dog is: {my_dog_2.breed}")

# Call the behavior (method) of each object
print(my_dog_1.bark())
print(my_dog_2.bark())