# Palindrome Checker

Checks if a word or phrase reads the same forwards and backwards. Ignores spaces, punctuation, and case — so "A man, a plan, a canal: Panama" is correctly identified as a palindrome.

## How to Run

```bash
python palindrome_checker.py
```

Type `quit` to exit.

## Example

```
Palindrome Checker
------------------------------

Enter a word or phrase (or 'quit' to exit): racecar
  'racecar' IS a palindrome!
  Cleaned: 'racecar' reversed is 'racecar'

Enter a word or phrase (or 'quit' to exit): A man, a plan, a canal: Panama
  'A man, a plan, a canal: Panama' IS a palindrome!
  Cleaned: 'amanaplanacanalpanama' reversed is 'amanaplanacanalpanama'

Enter a word or phrase (or 'quit' to exit): hello
  'hello' is NOT a palindrome.
  Cleaned: 'hello' reversed is 'olleh'
```

## What You'll Learn

- String slicing to reverse a string (`[::-1]`)
- Generator expressions for filtering characters
- `str.isalnum()` to check for letters and digits
- Separating logic into clean, reusable functions
