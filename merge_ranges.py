import unittest

def has_overlap(earliest_start, latest_end, meeting2):
    if earliest_start <= meeting2[0] <= latest_end:
        return True

    if meeting2[0] <= earliest_start <= meeting2[1]:
        return True

    return False

def merge_ranges(input_list):
    # Sort by start_time

    merged_ranges = []
    processed_indices = []
    for idx, meeting in enumerate(input_list):
        if idx in processed_indices:
            continue

        earliest_start = meeting[0]
        latest_end = meeting[1]
        for idx2, meeting2 in enumerate(input_list):
            if idx == idx2:
                continue

            if idx2 in processed_indices:
                continue

            if has_overlap(earliest_start, latest_end, meeting2):
                if meeting[0] < earliest_start:
                    earliest_start = meeting[0]

                if meeting2[0] < earliest_start:
                    earliest_start = meeting2[0]

                if meeting[1] > latest_end:
                    latest_end = meeting[1]

                if meeting2[1] > latest_end:
                    latest_end = meeting2[1]

                processed_indices.append(idx2)

        processed_indices.append(idx)
        merged_ranges.append((earliest_start, latest_end))

    merged_ranges = sorted(merged_ranges, key=lambda x: x[0])
    return merged_ranges



# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_one_long_meeting_contains_smaller_meetings(self):
        actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
        expected = [(1, 12)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)

    def test_touching_meetings(self):
        actual = merge_ranges([(1, 2), (2, 3)])
        expected = [(1, 3)]
        self.assertEqual(actual, expected)

    def test_subsumed_meeting(self):
        actual = merge_ranges([(1, 5), (2, 3)])
        expected = [(1, 5)]
        self.assertEqual(actual, expected)

    def test_more_multiple_meetings(self):
        actual = merge_ranges([(1, 10), (2, 6), (3, 5), (7, 9)])
        expected = [(1, 10)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
