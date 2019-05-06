import unittest
import math


def reverse_words(message):

    # Decode the message by reversing the words
    # until midpoint word is reached
    # swap words

    space_count = 0
    for letter in message:
        if letter == " ":
            space_count+=1

    word_count = space_count + 1
    midpoint_word_count = int(math.ceil(word_count/2.0))

    if word_count == 2:
        midpoint_word_count = word_count

    if word_count > 3 and word_count % 2 == 0:
        midpoint_word_count += 1

    last_idx = len(message) - 1

    for nth_word in range (1, midpoint_word_count):
        left_word_start = 0
        left_num_spaces = 0
        right_num_spaces = 0

        right_word_end = last_idx

        # Find nth left word
        for idx, letter in enumerate(message):
            if letter == " ":
                left_num_spaces += 1
                # If not the first word, and not the end of word space
                if nth_word != 1 and not left_num_spaces == nth_word:
                    left_word_start = idx + 1

            if left_num_spaces == nth_word:
                left_word_end = idx
                break


        # Save left word
        left_word = message[left_word_start:left_word_end]


        # Find nth right word
        for reverse_idx in range(last_idx, -1, -1):
            if message[reverse_idx] == " ":
                right_num_spaces += 1
                if nth_word != 1 and not right_num_spaces == nth_word:
                    right_word_end = reverse_idx - 1

            if right_num_spaces == nth_word:
                right_word_start = reverse_idx + 1
                break

        # Save right word
        right_word = message[right_word_start:(right_word_end + 1)]


        # delete
        del message[right_word_start:(right_word_end + 1)]
        del message[left_word_start:left_word_end]
        right_word_start -= len(left_word)

        # Swap
        left_word_last_idx = len(left_word) - 1
        for left_idx in range(left_word_last_idx, -1, -1):
            message.insert(right_word_start, left_word[left_idx])

        right_word_last_idx = len(right_word) - 1
        for right_idx in range(right_word_last_idx, -1, -1):
            message.insert(left_word_start, right_word[right_idx])


    pass

# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_even_num_multple_words(self):
        message = list('yummy is cake bundt chocolate yay')
        reverse_words(message)
        expected = list('yay chocolate bundt cake is yummy')
        self.assertEqual(message, expected)


    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)
