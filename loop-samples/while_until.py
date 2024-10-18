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
    
    if choice == 1:
        print("TODO: Implement Game 1")
    elif choice == 2:
        print("TODO: Implement Game 2")
    elif choice == 3:
        print("TODO: Implement Game 3")
    elif choice == 4:
        print("TODO: Implement Game 4")
    elif choice == 5:
        print("Exiting the program...")
    else:
        print("Invalid option, please choose between 1 and 5.")

