import unittest
from collections import Counter

def can_two_movies_fill_flight(movie_lengths, flight_length):
    # O(2n), can be done in O(n) with a set instead)

    # Determine if two movie runtimes add up to the flight length

    # Edge case: Less than two movies returns false
    if len(movie_lengths) < 2:
        return False


    film_counter = Counter()

    # build our film counter with num_minutes: count of films
    for movie_length in movie_lengths:
        film_counter[movie_length] += 1

    for movie_length in movie_lengths:

        # Edge case: if the movie is longer than or equal to the flight duration, skip
        if movie_length >= flight_length:
            continue

        # "Claim" the current film length
        film_counter[movie_length] -= 1

        remaining_length = flight_length - movie_length

        # No match found for the remaining length
        if film_counter[remaining_length] == 0:
            continue
        else:
            # match found!
            return True

    return False


# Tests

class Test(unittest.TestCase):

    def test_short_flight(self):
        result = can_two_movies_fill_flight([2, 4], 1)
        self.assertFalse(result)

    def test_long_flight(self):
        result = can_two_movies_fill_flight([2, 4], 6)
        self.assertTrue(result)

    def test_one_movie_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8], 6)
        self.assertFalse(result)

    def test_two_movies_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8, 3], 6)
        self.assertTrue(result)

    def test_lots_of_possible_pairs(self):
        result = can_two_movies_fill_flight([1, 2, 3, 4, 5, 6], 7)
        self.assertTrue(result)

    def test_not_using_first_movie(self):
        result = can_two_movies_fill_flight([4, 3, 2], 5)
        self.assertTrue(result)

    def test_only_one_movie(self):
        result = can_two_movies_fill_flight([6], 6)
        self.assertFalse(result)

    def test_no_movies(self):
        result = can_two_movies_fill_flight([], 2)
        self.assertFalse(result)


unittest.main(verbosity=2)
