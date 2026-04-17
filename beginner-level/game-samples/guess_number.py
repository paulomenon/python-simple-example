import random

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)
guess = 0
attempts = 0
    
print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Can you guess it?")
    
# Loop until the correct number is guessed
while guess != number_to_guess:
# Get the user's guess and convert it to an integer
    guess = int(input("Enter your guess: "))
    attempts += 1  # Increment attempts counter
        
    # Check if the guess is too high, too low, or correct
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        break