# Email Slicer (Username / Domain Extractor)
# Parses email addresses and extracts the username, domain name, and top-level domain.

def slice_email(email):
    """Parse an email into its components."""
    if "@" not in email or email.count("@") != 1:
        return None

    username, full_domain = email.split("@")

    if "." not in full_domain:
        return None

    parts = full_domain.rsplit(".", 1)
    domain_name = parts[0]
    tld = parts[1]

    return {
        "email": email,
        "username": username,
        "domain_name": domain_name,
        "tld": tld,
        "full_domain": full_domain,
    }


def display_result(result):
    """Display the parsed email components."""
    print(f"\n  Email:       {result['email']}")
    print(f"  Username:    {result['username']}")
    print(f"  Domain:      {result['domain_name']}")
    print(f"  TLD:         .{result['tld']}")
    print(f"  Full domain: {result['full_domain']}")


print("Email Slicer")
print("-" * 30)

while True:
    email = input("\nEnter an email address (or 'quit' to exit): ").strip()

    if email.lower() == "quit":
        print("Goodbye!")
        break

    result = slice_email(email)

    if result:
        display_result(result)
    else:
        print("  Invalid email format. Expected: user@domain.tld")
