'''
Regular expressions (regex) in Python are a powerful tool for matching patterns in text. Python provides the re module for working with regular expressions.

Basics of Regular Expressions

Literal Characters: Matches exactly the specified characters.
Meta Characters: Characters with special meaning in regex (e.g., ., ^, $, *, +, ?, {}, [], |, (), \).

Common Meta Characters
. : Matches any character except a newline.
^ : Matches the start of the string.
$ : Matches the end of the string.
* : Matches 0 or more repetitions of the preceding element.
+ : Matches 1 or more repetitions of the preceding element.
? : Matches 0 or 1 repetition of the preceding element.
{m,n} : Matches between m and n repetitions of the preceding element.
[] : Matches any single character inside the brackets.
| : Matches either the pattern before or after the |.
() : Groups patterns together and captures the matched text.
'''

# Email Validation Example

import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return True
    else:
        return False
emails = [
    "test@example.com",
    "user.name+tag+sorting@example.com",
    "user.name@sub.example.com",
    "user@123.123.123.123",
    "user@[IPv6:2001:db8::1]",
    "plainaddress",
    "@missingusername.com",
    "username@.com"
]

for email in emails:
    if validate_email(email):
        print(f"'{email}' is a valid email address.")
    else:
        print(f"'{email}' is not a valid email address.")

def extract_phone_numbers(text):
    # Define a regular expression pattern for matching phone numbers
    phone_number_pattern = re.compile(r'''
        # Match phone numbers in various formats
        (\+?\d{1,2})?                # Country code (optional)
        [\s.-]?                      # Separator (space, dot, or hyphen)
        \(?                          # Opening parenthesis (optional)
        (\d{3})                      # Area code (3 digits)
        \)?                          # Closing parenthesis (optional)
        [\s.-]?                      # Separator (space, dot, or hyphen)
        (\d{3})                      # First 3 digits
        [\s.-]?                      # Separator (space, dot, or hyphen)
        (\d{4})                      # Last 4 digits
    ''', re.VERBOSE)

    # Find all matches in the text
    matches = phone_number_pattern.findall(text)

    # Format the matches to standard phone number format
    phone_numbers = []
    for match in matches:
        country_code = match[0] if match[0] else ''
        area_code = match[1]
        first_three = match[2]
        last_four = match[3]
        phone_number = f"{country_code} ({area_code}) {first_three}-{last_four}" if country_code else f"({area_code}) {first_three}-{last_four}"
        phone_numbers.append(phone_number)
    
    return phone_numbers

# Example text containing phone numbers in various formats
text = """
Contact us at the following numbers:
- Office: (123) 456-7890
- Mobile: 123-456-7890
- Fax: 123.456.7890
- Hotline: 1234567890
- International: +1-123-456-7890
- Alternative: +91 987 654 3210
"""

# Extract and print phone numbers
phone_numbers = extract_phone_numbers(text)
for number in phone_numbers:
    print(number)