# An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.

# Examples of isograms:

# lumberjacks
# background
# downstream
# six-year-old
# The word isograms, however, is not an isogram, because the s repeats.

import itertools
import string


def is_isogram(text):
    # Keep only letters
    sorted_text = filter(lambda x: x in string.ascii_lowercase, text.lower())

    # Sort (needed for the group by)
    sorted_text = sorted(sorted_text)

    # Group by character
    g_data = itertools.groupby(sorted_text)

    # Check if all groups have a length of 1
    return all(len(list(group)) == 1 for _, group in g_data)


print(is_isogram("eleven"))
print(is_isogram("isograms"))
print(is_isogram("lumberjacks"))
