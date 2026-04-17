# Email Slicer (Username / Domain Extractor)

Parses an email address and extracts its components: username, domain name, and top-level domain. Includes basic validation.

## How to Run

```bash
python email_slicer.py
```

Type `quit` to exit.

## Example

```
Email Slicer
------------------------------

Enter an email address (or 'quit' to exit): john.doe@gmail.com

  Email:       john.doe@gmail.com
  Username:    john.doe
  Domain:      gmail
  TLD:         .com
  Full domain: gmail.com

Enter an email address (or 'quit' to exit): admin@company.co.uk

  Email:       admin@company.co.uk
  Username:    admin
  Domain:      company.co
  TLD:         .uk
  Full domain: company.co.uk

Enter an email address (or 'quit' to exit): invalid-email
  Invalid email format. Expected: user@domain.tld
```

## What You'll Learn

- String methods: `split()`, `rsplit()`, `count()`, `strip()`
- Input validation with conditional checks
- Returning structured data (dictionaries) from functions
- Looping until the user quits
