# ISBN
# The ISBN-10 format is 9 digits (0 to 9) plus one check character (either a digit or an X only).
# In the case the check character is an X, this represents the value '10'.
# These may be communicated with or without hyphens, and can be checked for their validity by the following formula:

# (d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0
# If the result is 0, then it is a valid ISBN-10, otherwise it is invalid.

# Example
# Let's take the ISBN-10 3-598-21508-8. We plug it in to the formula, and get:

# (3 * 10 + 5 * 9 + 9 * 8 + 8 * 7 + 2 * 6 + 1 * 5 + 5 * 4 + 0 * 3 + 8 * 2 + 8 * 1) mod 11 == 0
# Since the result is 0, this proves that our ISBN is valid.

import re


VALID_SPECIAL_CHECK_CHARACTER = "X"


def is_valid(isbn):
    isbn = isbn.replace("-", "")

    if len(isbn) != 10:
        return False

    match = check_pattern(isbn)
    if not match:
        return False

    print(isbn)

    return sum_digits_is_mod_11(isbn)


def sum_digits_is_mod_11(isbn):
    sum = 0
    for index in range(10):
        digitValue = get_digit_value(isbn, index)
        sum += (10 - index) * digitValue

    return sum % 11 == 0


def check_pattern(text):
    pattern = rf'^\d+({VALID_SPECIAL_CHECK_CHARACTER})?$'
    match = re.fullmatch(pattern, text)
    return match is not None


def get_digit_value(isbn, index):
    digit = isbn[index]
    if digit == "X":
        digit = "10"
    return int(digit)


# print(is_valid("3-598-21508-8"))


# print(is_valid("3-598-21508-9"))
