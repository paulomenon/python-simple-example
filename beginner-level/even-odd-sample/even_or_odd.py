# Check whether a number is even or odd using the modulo operator

number = int(input("Enter a number: "))

# A number is even if dividing by 2 leaves no remainder
if number % 2 == 0:
    print(f"{number} is Even.")
else:
    print(f"{number} is Odd.")
