EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int):
    """Calculate the preparation time.

    :param number_of_layers: int - number od layers to prepare.
    :return: int - preparation time (in minutes).

    Function that takes the number of layers minutes of the lasagna returns how many minutes the lasagna still needs to be prepared
    based on the `PREPARATION_TIME`.
    """

    return PREPARATION_TIME * number_of_layers