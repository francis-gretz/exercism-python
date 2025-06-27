# The Caesar cipher is a simple shift cipher that relies on transposing all the letters in the alphabet using an integer key between 0 and 26. Using a key of 0 or 26 will always yield the same output due to modular arithmetic. The letter is shifted for as many values as the value of the key.

# The general notation for rotational ciphers is ROT + <key>. The most commonly used rotational cipher is ROT13.

# A ROT13 on the Latin alphabet would be as follows:

# Plain:  abcdefghijklmnopqrstuvwxyz
# Cipher: nopqrstuvwxyzabcdefghijklm
# It is stronger than the Atbash cipher because it has 27 possible keys, and 25 usable keys.

# Ciphertext is written out in the same formatting as the input including spaces and punctuation.

# Examples
# ROT5 omg gives trl
# ROT0 c gives c
# ROT26 Cool gives Cool

import string

def rotate(text, key):
    """Caesar Cipher.
    Rotates (latin, unaccented) letters in text around the alphabet by key.
    Doesn't change other things.

    text: the string to rotate.
    key: the amount to rotate by.

    returns: the rotated string.
    """
    UPPERCASE = string.ascii_uppercase
    LOWERCASE = string.ascii_lowercase

    upper_shifted = UPPERCASE[key:] + UPPERCASE[:key]
    lower_shifted = LOWERCASE[key:] + LOWERCASE[:key]

    translation = str.maketrans(
        UPPERCASE + LOWERCASE, upper_shifted + lower_shifted)

    return text.translate(translation)


print(rotate("omg", 5))
