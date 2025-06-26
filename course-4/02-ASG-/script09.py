class Player:
    # When a new Player is created, the __init__ function will run.
    # 'self' here will be the newly created object (e.g., player1, player2).
    def __init__(self, name):
        # self.name will create a 'name' attribute for that SPECIFIC object.
        self.name = name
        self.score = 0
        print(f"Player {self.name} has joined the game!")

    # When calling player1.add_score(), 'self' inside this function is player1.
    def add_score(self, points_to_add):
        self.score = self.score + points_to_add
        print(f"-> {self.name} earned {points_to_add} points!")

    # When calling player2.show_score(), 'self' inside this function is player2.
    def show_score(self):
        print(f"CURRENT SCORE: {self.name} has {self.score} points.")


# --- GAME STARTS ---
# Create two separate instances from the Player class
player1 = Player("Alice")
player2 = Player("Bob")

print("\n--- ROUND 1 ---")
# When calling this function, self inside add_score() is 'player1'
player1.add_score(10)

# When calling this function, self inside add_score() is 'player2'
player2.add_score(5)

player1.show_score() # self is player1 -> "Alice has 10 points"
player2.show_score() # self is player2 -> "Bob has 5 points"

print("\n--- ROUND 2 ---")
# Alice scores again, Bob's score is not affected
player1.add_score(20)
player1.show_score() # self is player1 -> "Alice has 30 points"
player2.show_score() # self is player2 -> "Bob still has 5 points"