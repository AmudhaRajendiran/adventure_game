# adventure_game.py
# This script is a text-based adventure game where the player explores and finds treasure

print("Setup complete! Game file is working.")

#Create a function to start the game
def start_game():
    print("\n🌟 Welcome to the Adventure Game!")

    player_name = input("Enter your name: ")
    print(f"Hello {player_name}, your journey begins!")

    print("\nChoose your path:")
    print("1. Dark Forest 🌲")
    print("2. Mysterious Cave 🕳️")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        forest_path(player_name)
    elif choice == "2":
        cave_path(player_name)
    else:
        print("Invalid choice! Please try again.")
        start_game()

#Create the forest path
def forest_path(player_name):
    print("\n🌲 You entered the forest...")

    choice = input("Do you want to (1) follow a river or (2) climb a tree? ")

    if choice == "1":
        print("\nYou follow the river and discover a hidden treasure!")
        print(f"🎉 Congratulations {player_name}, you WIN!")
    elif choice == "2":
        print("\nYou fall from the tree and lose your way.")
        print("💀 Game Over!")
    else:
        print("Invalid choice.")

#Create the cave path
def cave_path(player_name):
    print("\n🕳️ You entered the cave...")

    choice = input("Do you want to (1) light a torch or (2) walk in the dark? ")

    if choice == "1":
        print("\nThe torch reveals a hidden door with treasure!")
        print(f"🎉 Congratulations {player_name}, you WIN!")
    elif choice == "2":
        print("\nYou fall into a pit.")
        print("💀 Game Over!")
    else:
        print("Invalid choice.")

#Start the game
def start_game():
    print("\n🌟 Welcome to the Adventure Game!")

    player_name = input("Enter your name: ")
    print(f"Hello {player_name}, your journey begins!")

    while True:
        print("\nChoose your path:")
        print("1. Dark Forest 🌲")
        print("2. Mysterious Cave 🕳️")

        choice = input("Enter 1 or 2: ")

        if choice == "1":
            forest_path(player_name)
        elif choice == "2":
            cave_path(player_name)
        else:
            print("Invalid choice.")
            continue

        restart = input("\nDo you want to play again? (yes/no): ").lower()

        if restart != "yes":
            print("Thanks for playing!")
            break
        
# Run the game
if __name__ == "__main__":
    start_game()    
