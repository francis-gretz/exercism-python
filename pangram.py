# A pangram is a sentence using every letter of the alphabet at least once. It is case insensitive, so it doesn't matter if a letter is lower-case (e.g. k) or upper-case (e.g. K).

# For this exercise, a sentence is a pangram if it contains each of the 26 letters in the English alphabet.

import string


def is_pangram(sentence):
    sentence_in_lower_case = sentence.lower()
    return all(char in sentence_in_lower_case for char in string.ascii_lowercase)


print(is_pangram("sentence"))
print(is_pangram("The quick brown fox jumps over the lazy dog."))
