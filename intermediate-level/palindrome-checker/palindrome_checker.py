# Palindrome Checker
# Checks if a word or phrase reads the same forwards and backwards.
# Ignores spaces, punctuation, and case.

def clean_text(text):
    """Remove everything except letters and numbers, then lowercase."""
    return "".join(char.lower() for char in text if char.isalnum())


def is_palindrome(text):
    """Check if the cleaned text is a palindrome."""
    cleaned = clean_text(text)
    return cleaned == cleaned[::-1]


print("Palindrome Checker")
print("-" * 30)

while True:
    text = input("\nEnter a word or phrase (or 'quit' to exit): ")

    if text.lower() == "quit":
        print("Goodbye!")
        break

    cleaned = clean_text(text)
    if is_palindrome(text):
        print(f"  '{text}' IS a palindrome!")
        print(f"  Cleaned: '{cleaned}' reversed is '{cleaned[::-1]}'")
    else:
        print(f"  '{text}' is NOT a palindrome.")
        print(f"  Cleaned: '{cleaned}' reversed is '{cleaned[::-1]}'")
