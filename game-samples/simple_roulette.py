import random

def roulette_color(number):
    """Return 'Red' or 'Black' based on the number."""
    # Roulette numbers 1 to 10 and 19 to 28:
    # odd numbers are red, even are black
    if (1 <= number <= 10) or (19 <= number <= 28):
        if number % 2 == 0:
            return 'Black'
        else:
            return 'Red'
    # Roulette numbers 11 to 18 and 29 to 36:
    # odd numbers are black, even are red
    elif (11 <= number <= 18) or (29 <= number <= 36):
        if number % 2 == 0:
            return 'Red'
        else:
            return 'Black'
    # 0 is a special case and is green
    return 'Green'

def play_roulette():
    print("Welcome to the Roulette Game!")
    print("Place your bet on a number (0-36):")

    # Player places bet
    try:
        player_bet = int(input("Enter your number: "))
        if player_bet < 0 or player_bet > 36:
            print("Please enter a number between 0 and 36.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # Spin the roulette
    roulette_number = random.randint(0, 36)
    roulette_color_result = roulette_color(roulette_number)

    # Determine if player won or lost
    if player_bet == roulette_number:
        print(f"Congratulations! You won!")
        print(f"The ball landed on {roulette_number} ({roulette_color_result}).")
    else:
        print(f"Sorry, you lost.")
        print(f"The ball landed on {roulette_number} ({roulette_color_result}).")

if __name__ == "__main__":
    play_roulette()
