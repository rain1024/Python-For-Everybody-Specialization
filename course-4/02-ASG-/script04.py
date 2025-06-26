# --- CLASS: COMPLETE RECIPE ---
# This is a "class" - a complete design blueprint.
# It contains ALL the ingredients (attributes) and steps to follow (methods).
# Like a piece of paper with a complete cake recipe.
class CakeRecipe:
    def __init__(self, cake_type, eggs, sugar_grams):
        """Constructor function, like listing the ingredients."""
        self.cake_type = cake_type
        self.eggs = eggs
        self.sugar = sugar_grams
        print(f"--- Starting to make '{self.cake_type}' with {self.eggs} eggs and {self.sugar}g sugar ---")

    def step1_mix_ingredients(self):
        """A method representing one step in the recipe."""
        print("DIRECTION 1: Mix eggs and sugar thoroughly in a large bowl.")

    def step2_add_flour(self):
        """Another method, another step."""
        print("DIRECTION 2: Add 200g flour and continue mixing.")

    def step3_bake_cake(self):
        """Final method."""
        print("DIRECTION 3: Pour mixture into pan and bake at 180°C for 20 minutes.")

# --- USING CLASS TO CREATE OBJECT ---
# Now we use the "CakeRecipe" blueprint to start a specific baking session.
sponge_cake_recipe = CakeRecipe("Sponge Cake", 4, 150)

print("\n--- EXECUTING EACH 'DIRECTION' (INSTRUCTION) ---")

# Each method call is like reading and following ONE "instruction".
# This is a "direction". It's an action, a step.
sponge_cake_recipe.step1_mix_ingredients()

# This is another "direction".
sponge_cake_recipe.step2_add_flour()

# And the final "direction".
sponge_cake_recipe.step3_bake_cake()