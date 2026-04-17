import random

def magic_8_ball():
    responses = [
        "Yes, definitely.",
        "Ask again later.",
        "Don't count on it.",
        "It is certain.",
        "My sources say no.",
        "Yes, in due time.",
        "Outlook not so good.",
        "Yes, absolutely.",
        "Better not tell you now.",
        "Very doubtful."
    ]

    print("Welcome to the Magic 8-Ball Game!")

    while True:
        question = input("What is your question? ")
        
        # Get a random response
        response = random.choice(responses)
        
        print(f"Magic 8-Ball says: {response}")

        # Ask if the player wants to play again
        play_again = input("Do you want to ask another question? (Yes/No): ").strip().lower()
        
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    magic_8_ball()
