import unittest
from fizzbuzz import fizzbuzz


class fizzbuzzTest(unittest.TestCase):

    def test_non_list_inputs(self):
        self.assertEqual(fizzbuzz(5, 8), "Invalid input")

    def test_non_list_input(self):
        self.assertEqual(fizzbuzz([2, 3, 4], 7), "Invalid input")

    def test_fizz(self):
        self.assertEqual(fizzbuzz([1, 3, 4], ['a', 'b', 'c']), "fizz")

    def test_buzz(self):
        self.assertEqual(fizzbuzz([4, 5, 4], [3, 4]), "buzz")

    def test_fizz_buzz(self):
        self.assertEqual(fizzbuzz([1, 2, 3, 3, 4, 5, 5, 5, 5, 6],
                                  [7, 7, 4, 5, 9]), "fizzbuzz")

    def test_other_total(self):
        self.assertEqual(fizzbuzz([4, 5, 6], [3]), 4)

    def test_both_empty(self):
        self.assertEqual(fizzbuzz([1, 3, 5], []), "fizz")
