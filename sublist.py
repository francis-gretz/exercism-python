"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
EQUAL = "="
SUBLIST = "-"
SUPERLIST = "+"
UNEQUAL = "!"


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL

    lenght_list_one = len(list_one)
    length_list_two = len(list_two)

    if (lenght_list_one >= length_list_two):
        if is_subset(list_one, list_two, lenght_list_one, length_list_two):
            return SUPERLIST
    else:
        if is_subset(list_two, list_one, length_list_two, lenght_list_one):
            return SUBLIST

    return UNEQUAL


def is_subset(list_a, list_b, length_a, length_b):
    if (length_b == 0):
        return True

    for i in range(length_a + 1 - length_b):
        subset = list_a[i: i + length_b]
        if (list_b == subset):
            return True
    return False


# result = is_subset([0, 1, 2, 3, 4, 5], [3, 4, 5], 6, 3)
# print(result)

result = sublist([], [1, 2, 3])
print(result)
