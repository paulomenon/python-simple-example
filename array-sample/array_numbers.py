def main():
    numbers = list(range(1, 21))  # Initialize an array with numbers from 1 to 20

    # Display current numbers the first time the program runs
    print("Current numbers:", numbers)

    while True:
        print("\nOptions:")
        print("1. Print only odd numbers")
        print("2. Print only even numbers")
        print("3. Remove a number")
        print("4. Add a number")
        print("5. Show current numbers")
        print("6. Exit")
        
        # Get user choice
        choice = input("Please select an option (1-6): ")

        if choice == '1':
            # Print only odd numbers
            odd_numbers = [num for num in numbers if num % 2 != 0]
            print("Odd numbers:", odd_numbers)

        elif choice == '2':
            # Print only even numbers
            even_numbers = [num for num in numbers if num % 2 == 0]
            print("Even numbers:", even_numbers)

        elif choice == '3':
            # Remove a number
            number_to_remove = int(input("Enter the number you want to remove: "))
            if number_to_remove in numbers:
                numbers.remove(number_to_remove)
                print(f"Number {number_to_remove} removed.")
            else:
                print(f"Number {number_to_remove} not found in the list.")

        elif choice == '4':
            # Add a number
            number_to_add = int(input("Enter the number you want to add: "))
            if number_to_add not in numbers:
                numbers.append(number_to_add)
                print(f"Number {number_to_add} added.")
            else:
                print(f"Number {number_to_add} is already in the list.")

        elif choice == '5':
            # Show current numbers
            print("\nCurrent numbers:", numbers)

        elif choice == '6':
            # Exit the program
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
