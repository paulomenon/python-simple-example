# Define the game functions
def game1():
    print("TODO: Implement Game 1")
    return_to_menu()

def game2():
    print("TODO: Implement Game 2")
    return_to_menu()

def game3():
    print("TODO: Implement Game 3")
    return_to_menu()

def game4():
    print("TODO: Implement Game 4")
    return_to_menu()

def exit_program():
    print("Exiting the program...")

# Function to return to the menu (option 0)
def return_to_menu():
    print("Press 0 to return to the menu.")
    while True:
        option = int(input("Enter 0 to go back: "))
        if option == 0:
            break  # Exit the loop to return to the main menu

# Function to display the game menu
def display_menu():
    print("Game Menu:")
    print("1. Game 1")
    print("2. Game 2")
    print("3. Game 3")
    print("4. Game 4")
    print("5. Exit")

# Main program loop
choice = 0
while choice != 5:
    display_menu()  # Show the menu
    choice = int(input("Choose an option (1-5): "))
    
    # Using match-case instead of if-else
    match choice:
        case 1:
            game1()
        case 2:
            game2()
        case 3:
            game3()
        case 4:
            game4()
        case 5:
            exit_program()
        case _:
            print("Invalid option, please choose between 1 and 5.")
