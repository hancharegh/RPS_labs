import unittest
from shaker_sort import shaker_sort


class TestShakerSort(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(shaker_sort([]), [])

    def test_single_element(self):
        self.assertEqual(shaker_sort([5]), [5])

    def test_sorted_array(self):
        self.assertEqual(shaker_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_reverse_array(self):
        self.assertEqual(shaker_sort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_random_array(self):
        self.assertEqual(shaker_sort([3, -1, 2, 0]), [-1, 0, 2, 3])


if __name__ == "__main__":
    unittest.main(verbosity=2)
