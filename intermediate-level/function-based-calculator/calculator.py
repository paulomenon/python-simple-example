# Function-Based Calculator
# Each operation is its own function. The program loops until the user quits.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def power(a, b):
    return a ** b

def modulo(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a % b

def display_menu():
    print("\n===== Calculator =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulo")
    print("7. Quit")
    print("======================")

# Map menu choices to functions
operations = {
    "1": ("Addition", add),
    "2": ("Subtraction", subtract),
    "3": ("Multiplication", multiply),
    "4": ("Division", divide),
    "5": ("Power", power),
    "6": ("Modulo", modulo),
}

while True:
    display_menu()
    choice = input("Choose an operation (1-7): ")

    if choice == "7":
        print("Goodbye!")
        break

    if choice not in operations:
        print("Invalid choice. Try again.")
        continue

    name, func = operations[choice]

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    result = func(num1, num2)
    print(f"\n{name}: {num1} and {num2} = {result}")
