# Instructions
# Your task is to determine what Bob will reply to someone when they say something to him or ask him a question.

# Bob only ever answers one of five things:

# "Sure." This is his response if you ask him a question, such as "How are you?" The convention used for questions is that it ends with a question mark.
# "Whoa, chill out!" This is his answer if you YELL AT HIM. The convention used for yelling is ALL CAPITAL LETTERS.
# "Calm down, I know what I'm doing!" This is what he says if you yell a question at him.
# "Fine. Be that way!" This is how he responds to silence. The convention used for silence is nothing, or various combinations of whitespace characters.
# "Whatever." This is what he answers to anything else.

QUESTION_ANSWER = "Sure."
YELL_ANSWER = "Whoa, chill out!"
YELL_QUESTION_ANSWER = "Calm down, I know what I'm doing!"
SILENCE_ANSWER = "Fine. Be that way!"
DEFAULT_ANSWER = "Whatever."


def is_a_question(hey_bob):
    return hey_bob.strip().endswith("?")


def contains_at_least_one_letter(hey_bob):
    return any(c.isalpha() for c in hey_bob)


def is_a_yell(hey_bob):
    return contains_at_least_one_letter(hey_bob) and hey_bob.isupper()


def is_a_silence(hey_bob):
    return not hey_bob


def response(hey_bob):
    hey_bob = hey_bob.strip()

    if is_a_silence(hey_bob):
        return SILENCE_ANSWER

    question = is_a_question(hey_bob)
    yell = is_a_yell(hey_bob)

    if not (question or yell):
        return DEFAULT_ANSWER

    if yell and question:
        return YELL_QUESTION_ANSWER

    if not yell and question:
        return QUESTION_ANSWER

    return YELL_ANSWER
