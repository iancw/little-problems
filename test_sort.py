import unittest
from no_fours import brute, fast
from sort import quicksort, mergesort

class TestSort(unittest.TestCase):

	def test_quick(self):
		#self.assertEqual([1,2,3,5,7,9], quicksort([1, 5, 2, 9, 3, 7]))
		pass

	def test_merge(self):
		self.assertEqual([1,2,3,5,7,9], mergesort([1, 5, 2, 9, 3, 7]))
		self.assertEqual([1,2,3,7,9], mergesort([1, 2, 3, 7, 9]))
		self.assertEqual(range(0, 10), mergesort(range(0,10)[::-1]))
		self.assertEqual([1], mergesort([1]))
		self.assertEqual([], mergesort([]))

if __name__ == '__main__':
	unittest.main()