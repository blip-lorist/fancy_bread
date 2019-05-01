import unittest
import math


def reverse(list_of_chars):
    # [A, B, C, D, E]
    # [E, D, C, B, A]

    midpoint = int(math.ceil(len(list_of_chars) / 2))
    # Odd case
    # [A, B, C, D, E]
    #        ^


    if midpoint % 2 == 0:
        midpoint += 1
    # Even case
    # [A, B, C, D]
    #        ^


    # Only walk up to midpoint
    for idx in range(1, midpoint):
        left_idx = idx-1
        right_idx = -idx
        list_of_chars[left_idx], list_of_chars[right_idx] = list_of_chars[right_idx], list_of_chars[left_idx]

    pass

# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_odd_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)


    def test_even_string(self):
        list_of_chars = ['A', 'B', 'C', 'D']
        reverse(list_of_chars)
        expected = ['D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)


unittest.main(verbosity=2)
