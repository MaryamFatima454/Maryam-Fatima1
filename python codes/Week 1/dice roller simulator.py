
import random

print(" Welcome to the Dice Roller Simulator!")

while True:
    input("Press Enter to roll the dice...")
    dice = random.randint(1, 6)  # Generates a number between 1 and 6
    print("You rolled a", dice)
    
    again = input("Roll again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing! Goodbye!")
        break

