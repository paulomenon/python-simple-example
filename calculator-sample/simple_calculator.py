# Simple calculator that performs basic arithmetic operations
# Supports addition, subtraction, multiplication, and division

print("Simple Calculator")
print("-" * 30)

# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Show available operations
print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("\nEnter your choice (1/2/3/4): ")

# Perform the selected operation
if choice == "1":
    result = num1 + num2
    print(f"\n{num1} + {num2} = {result}")
elif choice == "2":
    result = num1 - num2
    print(f"\n{num1} - {num2} = {result}")
elif choice == "3":
    result = num1 * num2
    print(f"\n{num1} * {num2} = {result}")
elif choice == "4":
    if num2 == 0:
        print("\nError: Cannot divide by zero!")
    else:
        result = num1 / num2
        print(f"\n{num1} / {num2} = {result}")
else:
    print("\nInvalid choice. Please enter 1, 2, 3, or 4.")
