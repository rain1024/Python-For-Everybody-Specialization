# This is the DESIGN BLUEPRINT, the definition of the CLASS
# It defines the "structure" (rooms, paint_color)
# and "capabilities" (open_door, turn_on_light)
class House:
    # Constructor method to set up initial state
    def __init__(self, address, rooms, paint_color):
        print(f"Building a house at {address}...")
        self.address = address
        self.rooms = rooms
        self.paint_color = paint_color
        self.light_on = False # Light is off initially

    # A method that represents "capability"
    def turn_on_light(self):
        if not self.light_on:
            print("Light turned on!")
            self.light_on = True
        else:
            print("Light is already on.")

# --- OBJECT CREATION PROCESS BEGINS ---
# Python looks at the "class House" definition to know how to create objects
print("Starting to build my house.")
my_house = House("123 ABC Street", 4, "Blue")

print("\nStarting to build neighbor's house.")
neighbor_house = House("125 ABC Street", 5, "Yellow")

# Each object has its own structure, defined by the class
print(f"\nMy house has {my_house.rooms} rooms and is painted {my_house.paint_color}.")
print(f"Neighbor's house has {neighbor_house.rooms} rooms and is painted {neighbor_house.paint_color}.")

# Objects have the same "capabilities" (methods)
my_house.turn_on_light() # Output: Light turned on!
my_house.turn_on_light() # Output: Light is already on.