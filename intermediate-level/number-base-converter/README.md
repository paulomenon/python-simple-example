# Number Base Converter (Binary / Denary / Hex)

Converts numbers between binary (base 2), denary/decimal (base 10), and hexadecimal (base 16). Enter a number in any base and see it displayed in all three.

## How to Run

```bash
python base_converter.py
```

## Example

```
Number Base Converter
------------------------------
1. Denary → Binary & Hex
2. Binary → Denary & Hex
3. Hexadecimal → Denary & Binary

Choose a conversion (1/2/3): 1
Enter a denary (decimal) number: 255

  Denary (base 10):      255
  Binary (base 2):       11111111
  Hexadecimal (base 16): FF
```

```
Choose a conversion (1/2/3): 2
Enter a binary number: 10101010

  Denary (base 10):      170
  Binary (base 2):       10101010
  Hexadecimal (base 16): AA
```

## What You'll Learn

- Python built-in functions: `bin()`, `hex()`, `int()` with a base argument
- String slicing to remove prefixes
- Input validation for binary strings
