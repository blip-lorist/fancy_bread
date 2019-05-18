words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

# Binary search
# The needle in the haystack is:
# Finding the smallest a-z value
# neighboring the largest a-z value

import unittest

def find_rotation_point(words):

    # Find the rotation point in the list

    floor_idx = 0
    ceiling_idx = len(words) - 1

    while floor_idx < ceiling_idx:
        list_size = ceiling_idx - floor_idx
        half_size = list_size // 2
        midpoint_idx = floor_idx + half_size

        midpoint_word = words[midpoint_idx]

        previous_idx = midpoint_idx - 1
        later_idx = midpoint_idx + 1
        previous_word = words[previous_idx]
        later_word = words[later_idx]

        first_word = words[floor_idx]
        end_word = words[ceiling_idx]

        # Check if we've found the needle in the haystack
        if previous_word > midpoint_word:
            return midpoint_idx
        elif midpoint_word > later_word:
            return later_idx
        else:
            # keep lookin'
            if midpoint_word > first_word:
                # Go right
                floor_idx = midpoint_idx
            else:
                # Go left
                ceiling_idx = midpoint_idx



# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)
