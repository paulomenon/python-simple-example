# Caesar Cipher Encoder/Decoder
# Shifts each letter by a fixed number of positions in the alphabet.
# For example, with a shift of 3: A→D, B→E, C→F, ..., Z→C

def caesar_encrypt(text, shift):
    """Encrypt text using a Caesar cipher with the given shift."""
    result = []
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return "".join(result)


def caesar_decrypt(text, shift):
    """Decrypt by shifting in the opposite direction."""
    return caesar_encrypt(text, -shift)


print("Caesar Cipher")
print("-" * 30)
print("1. Encrypt")
print("2. Decrypt")

choice = input("\nChoose (1/2): ")
text = input("Enter your message: ")

try:
    shift = int(input("Enter shift value (1-25): "))
except ValueError:
    print("Invalid shift. Please enter a number.")
    exit()

if shift < 1 or shift > 25:
    print("Shift must be between 1 and 25.")
elif choice == "1":
    encrypted = caesar_encrypt(text, shift)
    print(f"\nOriginal:  {text}")
    print(f"Encrypted: {encrypted}")
elif choice == "2":
    decrypted = caesar_decrypt(text, shift)
    print(f"\nEncrypted: {text}")
    print(f"Decrypted: {decrypted}")
else:
    print("Invalid choice.")
