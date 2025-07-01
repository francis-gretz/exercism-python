def get_dictionary_from_text(text):
    text = text.lower()

    text_set = set(text)

    dictionary = dict()
    for ch in text_set:
        dictionary[ch] = text.count(ch)

    return dictionary


def find_anagrams(word, candidates):
    word_dictionary = get_dictionary_from_text(word)
    word_in_lower_case = word.lower()

    result = []
    for candidate in candidates:
        # A word is not its own anagram
        if candidate.lower() == word_in_lower_case:
            continue

        candidate_dictionary = get_dictionary_from_text(candidate)
        if candidate_dictionary == word_dictionary:
            result.append(candidate)

    return result
