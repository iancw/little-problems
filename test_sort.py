import unittest
from no_fours import brute, fast
from sort import quicksort, mergesort

class TestSort(unittest.TestCase):

	def test_quick(self):
		ar = [1, 5, 2, 9, 3, 7]
		quicksort(ar)
		self.assertEqual([1,2,3,5,7,9], ar)

def test_merge(self):
		ar = [1, 5, 2, 9, 3, 7]
		mergesort(ar)
		self.assertEqual([1,2,3,5,7,9], ar)

if __name__ == '__main__':
	unittest.main()