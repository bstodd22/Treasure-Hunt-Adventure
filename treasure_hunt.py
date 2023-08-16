class TreasureHuntGame:
    def __init__(self):
        # Initialize two data structures to hold clues for stack and queue paths
        self.clues_stack = []  # Clues for stack path
        self.clues_queue = []  # Clues for queue path

    def add_clue_to_stack(self, clue):
        # Add a clue to the stack path
        self.clues_stack.append(clue)

    def add_clue_to_queue(self, clue):
        # Add a clue to the queue path
        self.clues_queue.append(clue)

    # This function begins the game
    def start_game(self):
        print(
            '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
        )
        print("Welcome to Treasure Island.")
        print("Your mission is to find the treasure.")

        # The user chooses which path they want to take
        choice = input("Enter 'left' or 'right' to choose a path: ")

        if choice.lower() == "left":
            self.follow_stack_path()
        elif choice.lower() == "right":
            self.follow_queue_path()
        else:
            print("Invalid option. Game Over.")

    def follow_stack_path(self):
        print("You've chosen the stack path!")
        print("Following the clues for a stack: ")

        while self.clues_stack:
            clue = self.clues_stack.pop()  # Get the top clue from the stack
            print(f"Clue: {clue}")
            action = input("Do you want to continue? (y/n): ")
            if action.lower() != "y":
                print("Game over.")
                return

        print("Congratulations! You've reached the treasure!")

    def follow_queue_path(self):
        print("You've chosen the queue path!")
        print("Following the clues using queue: ")

        while self.clues_queue:
            clue = self.clues_queue.pop(0)  # Get the front clue from the queue
            print(f"Clue: {clue}")
            action = input("Do you want to continue? (y/n): ")
            if action.lower() != "y":
                print("Game over.")
                return

        print("Congratulations! You've reached the treasure!")


if __name__ == "__main__":
    game = TreasureHuntGame()

    # Adding clues to the stack path
    game.add_clue_to_stack("Start at the big oak tree.")
    game.add_clue_to_stack("Go 10 steps east.")
    game.add_clue_to_stack("Turn left and walk to the river.")
    game.add_clue_to_stack("Cross the bridge and head towards the mountain.")

    # Adding clues to the queue path
    game.add_clue_to_queue("Start at the old windmill.")
    game.add_clue_to_queue("Walk straight to the stone well.")
    game.add_clue_to_queue("Turn right and follow the winding path.")
    game.add_clue_to_queue("Climb up the hill to the ancient ruins.")

    game.start_game()
