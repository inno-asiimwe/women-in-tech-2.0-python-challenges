import unittest

from list_sort import list_sort


class listsortTest(unittest.TestCase):

    def test_integer_input(self):
        self.assertEqual(list_sort(5), 'Invalid Input')

    def test_string_input(self):
        self.assertEqual(list_sort('string'), 'Invalid Input')

    def test_empty_list(self):
        self.assertEqual(list_sort([]), {'evens': [], 'odds': [], 'chars': []})

    def test_no_string(self):
        self.assertEqual(
            list_sort([4, 3, 2]),
            {'evens': [2, 4], 'odds': [3], 'chars': []}
            )

    def test_no_even(self):
        self.assertEqual(
            list_sort([9, 3, 5, 1, 'd', 'a']),
            {'evens': [], 'odds': [1, 3, 5, 9], 'chars': ['a', 'd']}
            )

    def test_no_odd(self):
        self.assertEqual(
            list_sort([10, 2, 8, 'c', 'f']),
            {'evens': [2, 8, 10], 'odds': [], 'chars': ['c', 'f']}
            )

    def test_complete_list(self):
        self.assertEqual(
            list_sort([4, 9, 2, 3, 5, 1, 'd', 'a', 'c', 'f']),
            {'evens': [2, 4], 'odds': [1, 3, 5, 9], 'chars': ['a', 'c', 'd', 'f']}
            )
    