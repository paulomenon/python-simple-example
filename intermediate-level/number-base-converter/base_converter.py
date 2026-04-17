# Number Base Converter
# Converts numbers between binary (base 2), denary/decimal (base 10), and hexadecimal (base 16).

def denary_to_binary(n):
    return bin(n)[2:]  # Remove '0b' prefix

def denary_to_hex(n):
    return hex(n)[2:].upper()  # Remove '0x' prefix, uppercase

def binary_to_denary(b):
    return int(b, 2)

def hex_to_denary(h):
    return int(h, 16)

def display_all_bases(denary_value):
    """Display a number in all three bases."""
    print(f"\n  Denary (base 10):      {denary_value}")
    print(f"  Binary (base 2):       {denary_to_binary(denary_value)}")
    print(f"  Hexadecimal (base 16): {denary_to_hex(denary_value)}")


print("Number Base Converter")
print("-" * 30)
print("1. Denary → Binary & Hex")
print("2. Binary → Denary & Hex")
print("3. Hexadecimal → Denary & Binary")

choice = input("\nChoose a conversion (1/2/3): ")

try:
    if choice == "1":
        value = int(input("Enter a denary (decimal) number: "))
        display_all_bases(value)

    elif choice == "2":
        value = input("Enter a binary number: ")
        # Validate binary input
        if not all(c in "01" for c in value):
            print("Error: Binary numbers can only contain 0 and 1.")
        else:
            denary = binary_to_denary(value)
            display_all_bases(denary)

    elif choice == "3":
        value = input("Enter a hexadecimal number: ")
        denary = hex_to_denary(value)
        display_all_bases(denary)

    else:
        print("Invalid choice.")

except ValueError:
    print("Error: Invalid number format.")
