class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_running = False

    def start_engine(self):
        """Method to start the car engine."""
        self.is_running = True
        print(f"Car {self.brand} {self.model} has started!")

    def stop_engine(self):
        """Method to stop the car engine."""
        self.is_running = False
        print(f"Car {self.brand} {self.model} has stopped.")

# Create a Car object
my_car = Car("VinFast", "VF8")

# Use dir() function to see what's inside the my_car object
print("--- Results from dir(my_car) function: ---")
print(dir(my_car))

print("\n--- Analysis of results: ---")
print("You can see the attributes we defined: 'brand', 'model', 'is_running'")
print("And the methods we defined: 'start_engine', 'stop_engine'")
print("Along with many special attributes starting with '__' like '__init__', '__dict__', etc.")

print("\n--- Functions used for wrong choices: ---")
# To see the type of object -> use type() function
print(f"Type of my_car: {type(my_car)}")

# To see parent class -> use __bases__ attribute
# Car class doesn't inherit from any other class, so Python will default it to inherit from 'object'
print(f"Parent class of Car: {Car.__bases__}")