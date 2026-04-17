# Generate a multiplication table for any number

number = int(input("Enter a number to see its multiplication table: "))

print(f"\nMultiplication Table for {number}")
print("-" * 25)

# Loop from 1 to 12 and print each multiplication
for i in range(1, 13):
    result = number * i
    print(f"{number} x {i:2d} = {result}")
