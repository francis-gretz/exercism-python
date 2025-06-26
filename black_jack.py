"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

ACE = "A"
FACES = ["J", "Q", "K", "10"]
NORMAL = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]


def is_face_card(card):
    return card in FACES


def is_ace_card(card):
    return card == ACE


def is_normal_card(card):
    return card in NORMAL


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if is_normal_card(card):
        return int(card)

    if is_face_card(card):
        return 10

    # case A
    return 1


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one == value_two:
        return (card_one, card_two)

    if value_one > value_two:
        return card_one

    return card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    if is_ace_card(card_one) or is_ace_card(card_two):
        return 1

    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    sum_of_cards = value_one + value_two
    if (21 - sum_of_cards) >= 11:
        return 11

    return 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    is_ace_one = is_ace_card(card_one)
    is_ace_two = is_ace_card(card_two)

    if is_ace_one and is_ace_two:
        return False

    if is_ace_one and not is_ace_two:
        return is_face_card(card_two)

    if is_ace_two and not is_ace_one:
        return is_face_card(card_one)

    return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    return value_one == value_two


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    sum_of_cards = value_one + value_two

    return 9 <= sum_of_cards <= 11
