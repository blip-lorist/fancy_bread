import unittest


def merge_lists(my_list, alices_list):

	# Sort both lists before starting
    # O(nlogn)
    my_list = sorted(my_list)
    alices_list = sorted(alices_list)
    merged_list = []


    my_list_length = len(my_list)
    alices_list_length = len(alices_list)

	# While either list has elements:
    while my_list_length > 0 or alices_list_length > 0:

        # Short circuit if one or the other is empty
        if my_list_length == 0 and alices_list_length > 0:
            merged_list.extend(alices_list)
            return merged_list

        if alices_list_length == 0 and my_list_length > 0:
            merged_list.extend(my_list)
            return merged_list


		# Compare first el of each list
        smallest_my_list_element = my_list[0]
        smallest_alice_list_element = alices_list[0]

        if smallest_my_list_element < smallest_alice_list_element:
            merged_list.append(my_list.pop(0))
        else:
            merged_list.append(alices_list.pop(0))

        # Update list lengths
        my_list_length = len(my_list)
        alices_list_length = len(alices_list)


	# Return merged list
    return merged_list

# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
