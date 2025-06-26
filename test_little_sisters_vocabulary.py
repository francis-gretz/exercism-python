import unittest

from little_sisters_vocabulary import (
    adjective_to_verb,
)


class LittleSistersVocabularyTest(unittest.TestCase):
    def test_asymmetric_position_between_the_inner_and_middle_circles(self):
        input_data = ['Look at the bright sky.',
                      'His expression went dark.',
                      'The bread got hard after sitting out.',
                      'The butter got soft in the sun.',
                      'Her eyes were light blue.',
                      'The morning fog made everything damp with mist.',
                      'He cut the fence pickets short by mistake.',
                      'Charles made weak crying noises.',
                      'The black oil got on the white dog.']
        index_data = [-2, -1, 3, 3, -2, -3, 5, 2, 1]
        result_data = ['brighten', 'darken', 'harden', 'soften',
                       'lighten', 'dampen', 'shorten', 'weaken', 'blacken']

        for variant, (sentence, index, expected) in enumerate(zip(input_data, index_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', sentence=sentence, index=index, expected=expected):
                actual_result = adjective_to_verb(sentence, index)
                error_message = (f'Called adjective_to_verb("{sentence}", {index}). '
                                 f'The function returned "{actual_result}", but the tests '
                                 f'expected "{expected}" as the verb for '
                                 f'the word at index {index}.')

            self.assertEqual(actual_result, expected, msg=error_message)
