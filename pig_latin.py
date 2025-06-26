# Instructions
# Your task is to translate text from English to Pig Latin. The translation is defined using four rules, which look at the pattern of vowels and consonants at the beginning of a word. These rules look at each word's use of vowels and consonants:

# vowels: the letters a, e, i, o, and u
# consonants: the other 21 letters of the English alphabet


# Rule 1
# If a word begins with a vowel, or starts with "xr" or "yt", add an "ay" sound to the end of the word.

# For example:

# "apple" -> "appleay" (starts with vowel)
# "xray" -> "xrayay" (starts with "xr")
# "yttria" -> "yttriaay" (starts with "yt")


# Rule 2
# If a word begins with one or more consonants, first move those consonants to the end of the word and then add an "ay" sound to the end of the word.

# For example:

# "pig" -> "igp" -> "igpay" (starts with single consonant)
# "chair" -> "airch" -> "airchay" (starts with multiple consonants)
# "thrush" -> "ushthr" -> "ushthray" (starts with multiple consonants)


# Rule 3
# If a word starts with zero or more consonants followed by "qu", first move those consonants (if any) and the "qu" part to the end of the word, and then add an "ay" sound to the end of the word.

# For example:

# "quick" -> "ickqu" -> "ickquay" (starts with "qu", no preceding consonants)
# "square" -> "aresqu" -> "aresquay" (starts with one consonant followed by "qu")


# Rule 4
# If a word starts with one or more consonants followed by "y", first move the consonants preceding the "y"to the end of the word, and then add an "ay" sound to the end of the word.

# Some examples:

# "my" -> "ym" -> "ymay" (starts with single consonant followed by "y")
# "rhythm" -> "ythmrh" -> "ythmrhay" (starts with multiple consonants followed by "y")

import re

# Constants
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def add_ay_to_starting_vowel_or_xr_yt(text):
    # rule 1
    match = re.match(rf'^(?:[{VOWELS}]|xr|yt)', text, re.IGNORECASE)
    if match:
        return True, text + "ay"
    return False, text


def move_starting_consonants_to_end(text):
    # rule 2
    match = re.match(
        rf'^([{CONSONANTS}]+)(.*)', text, re.IGNORECASE)
    if match:
        return True, match.group(2) + match.group(1) + "ay"
    return False, text


def move_starting_consonants_and_qu_to_end(text):
    # rule 3
    match = re.match(
        rf'^([{CONSONANTS}]*)(qu)(.*)', text, re.IGNORECASE)
    if match:
        return True, match.group(3) + match.group(1) + match.group(2) + "ay"
    return False, text


def move_starting_consonants_and_y_to_end(text):
    # rule 4
    match = re.match(
        rf'^([{CONSONANTS}]+)(y)(.*)', text, re.IGNORECASE)
    if match:
        return True, match.group(2) + match.group(3) + match.group(1) + "ay"
    return False, text


def translate_word(text):
    is_applied, result = add_ay_to_starting_vowel_or_xr_yt(text)
    if is_applied:
        return result

    is_applied, result = move_starting_consonants_and_qu_to_end(text)
    if is_applied:
        return result

    is_applied, result = move_starting_consonants_and_y_to_end(text)
    if is_applied:
        return result

    is_applied, result = move_starting_consonants_to_end(text)
    if is_applied:
        return result


def translate(text):
    words = text.split(" ")

    result = []
    for word in words:
        result.append(translate_word(word))

    return " ".join(result)


# print(move_starting_consonants_to_end("banana"))
# print(move_starting_consonants_to_end("thrush"))

# print(move_starting_consonants_and_qu_to_end("quick"))
# print(move_starting_consonants_and_qu_to_end("square"))

# print(move_starting_consonants_and_y_to_end("rhythm"))
print(translate("queen"))
