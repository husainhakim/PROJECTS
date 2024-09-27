import random

# Game introduction
print("|", "-" * 10, "Welcome to the number guessing game", "-" * 10, "|")
print("|", "I'm thinking of a number between 1 and 100.", " " * 13, "|")
print("|", "If you guess it correctly, you win!", " " * 21, "|")
print("-" * 61)
print("You will have a limited number of chances depending on the difficulty.")
print("Let's start!")

# Select difficulty level
print("Please select the difficulty level:")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)")
difficulty = int(input("Enter your choice: "))

# Setting the number of attempts based on difficulty
attempts = 0
if difficulty == 1:
    attempts = 10
elif difficulty == 2:
    attempts = 5
elif difficulty == 3:
    attempts = 3
else:
    print("Invalid choice! Defaulting to Medium difficulty.")
    attempts = 5

print(f"\nGreat! You have selected {'Easy' if difficulty == 1 else 'Medium' if difficulty == 2 else 'Hard'} difficulty.")
print(f"You have {attempts} chances to guess the correct number. Let's start the game!\n")

# Randomly selecting the number
secret_number = random.randint(1, 100)
guess = None
attempt_count = 0

# Main game loop
while attempts > 0:
    guess = int(input("Enter your guess: "))
    attempt_count += 1
    attempts -= 1
    
    if guess == secret_number:
        print(f"Congratulations! You guessed the correct number in {attempt_count} attempts.")
        break
    elif guess > secret_number:
        print(f"Incorrect! The number is less than {guess}.")
    else:
        print(f"Incorrect! The number is greater than {guess}.")
    
    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}. Better luck next time!")

# End of game