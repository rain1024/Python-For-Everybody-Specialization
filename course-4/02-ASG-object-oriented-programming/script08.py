# Define Robot class
class Robot:
    # Constructor method also starts with 'def'
    def __init__(self, name):
        self.name = name
        print(f"Robot {self.name} has been activated!")

    # 'greet' method, starts with keyword 'def'
    def greet(self):
        print(f"{self.name}: Hello world! I am {self.name}.")

    # 'move' method, also starts with 'def'
    def move(self, direction):
        print(f"{self.name} is moving towards {direction}.")

    # 'calculate_sum' method, also starts with 'def'
    def calculate_sum(self, num1, num2):
        result = num1 + num2
        print(f"{self.name}: The sum of {num1} and {num2} is {result}.")
        return result

# Create a Robot object
terminator = Robot("T-800")

# Call object methods
terminator.greet()
terminator.move("forward")
terminator.calculate_sum(1024, 2048)