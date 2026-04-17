# Fibonacci Sequence Generator
# Generates the Fibonacci sequence up to a user-specified number of terms.
# Each number is the sum of the two preceding ones: 0, 1, 1, 2, 3, 5, 8, ...

def generate_fibonacci(n):
    """Generate a list of the first n Fibonacci numbers."""
    if n <= 0:
        return []
    if n == 1:
        return [0]

    sequence = [0, 1]
    for _ in range(2, n):
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)

    return sequence


print("Fibonacci Sequence Generator")
print("-" * 30)

try:
    count = int(input("How many Fibonacci numbers to generate? "))
except ValueError:
    print("Please enter a valid integer.")
    exit()

if count <= 0:
    print("Please enter a positive number.")
else:
    sequence = generate_fibonacci(count)

    print(f"\nFirst {count} Fibonacci number(s):")
    print(", ".join(str(n) for n in sequence))

    print(f"\nThe {count}th Fibonacci number is: {sequence[-1]}")
    print(f"Sum of the sequence: {sum(sequence)}")
