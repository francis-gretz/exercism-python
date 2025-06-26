NUMBER_OF_SQUARES: int = 64


def square(number):
    # when the square value is not in the acceptable range
    if number < 1 or number > NUMBER_OF_SQUARES:
        raise ValueError(f"square must be between 1 and {NUMBER_OF_SQUARES}")

    return 2 ** (number - 1)


def total():
    return (2 ** NUMBER_OF_SQUARES) - 1
