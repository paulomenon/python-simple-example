def main():
    # Initialize a list of names
    names = ["Alice", "Bob", "Charlie", "David", "Eve"]

    while True:
        print("\nCurrent names:", names)
        print("\nOptions:")
        print("1. Add a name")
        print("2. Remove a name")
        print("3. Find a name")
        print("4. Exit")

        # Get user choice
        choice = input("Please select an option (1-4): ")

        if choice == '1':
            # Add a name
            name_to_add = input("Enter the name you want to add: ")
            if name_to_add not in names:
                names.append(name_to_add)
                print(f"Name '{name_to_add}' added.")
            else:
                print(f"Name '{name_to_add}' is already in the list.")

        elif choice == '2':
            # Remove a name
            name_to_remove = input("Enter the name you want to remove: ")
            if name_to_remove in names:
                names.remove(name_to_remove)
                print(f"Name '{name_to_remove}' removed.")
            else:
                print(f"Name '{name_to_remove}' not found in the list.")

        elif choice == '3':
            # Find a name
            name_to_find = input("Enter the name you want to find: ")
            if name_to_find in names:
                print(f"Name '{name_to_find}' found in the list.")
            else:
                print(f"Name '{name_to_find}' not found in the list.")

        elif choice == '4':
            # Exit the program
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
