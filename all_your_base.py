def rebase(input_base, digits, output_base):
    check_inputs(input_base, digits, output_base)

    input_number = from_base(digits, input_base)

    return to_base(input_number, output_base)


def check_inputs(input_base, digits, output_base):
    # for input.
    if (input_base < 2):
        raise ValueError("input base must be >= 2")

    # or, for output.
    if (output_base < 2):
        raise ValueError("output base must be >= 2")

    for digit in digits:
        # another example for input.
        if not (0 <= digit < input_base):
            raise ValueError("all digits must satisfy 0 <= d < input base")


def to_base(number, base):
    """Converts a non-negative number to a list of digits in the given base.

    The base must be an integer greater than or equal to 2 and the first digit
    in the list of digits is the most significant one.
    """
    if not number:
        return [0]

    digits = []
    while number:
        digits.append(number % base)
        number //= base
    return list(reversed(digits))


def from_base(digits, base):
    """Converts a list of digits in the given base to an integer.

    The first digit is the most significant and the base is assumed to
    be an integer greater than or equal to 2.
    """
    power = 1
    number = 0
    for digit in reversed(digits):
        number += power * digit
        power *= base
    return number
