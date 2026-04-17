# Caesar Cipher Encoder/Decoder

Encrypts and decrypts messages by shifting each letter a fixed number of positions in the alphabet. Numbers, spaces, and punctuation are left unchanged.

## How to Run

```bash
python caesar_cipher.py
```

## Example

```
Caesar Cipher
------------------------------
1. Encrypt
2. Decrypt

Choose (1/2): 1
Enter your message: Hello, World!
Enter shift value (1-25): 3

Original:  Hello, World!
Encrypted: Khoor, Zruog!
```

```
Choose (1/2): 2
Enter your message: Khoor, Zruog!
Enter shift value (1-25): 3

Encrypted: Khoor, Zruog!
Decrypted: Hello, World!
```

## What You'll Learn

- `ord()` and `chr()` for converting between characters and ASCII values
- Modular arithmetic (`% 26`) to wrap around the alphabet
- Preserving case (uppercase/lowercase) during encryption
- Decryption as the reverse of encryption (negative shift)
