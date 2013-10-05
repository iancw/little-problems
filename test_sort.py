import unittest
from no_fours import brute, fast
from sort import heapsort, mergesort

class TestSort(unittest.TestCase):

	def test_heap(self):
		self.help_sort(heapsort)

	def test_merge(self):
		self.help_sort(mergesort)

	def help_sort(self, sort):
		self.assertEqual([1,2,3,5,7,9], sort([1, 5, 2, 9, 3, 7]))
		self.assertEqual([1,2,3,7,9], sort([1, 2, 3, 7, 9]))
		self.assertEqual(range(0, 10), sort(range(0,10)[::-1]))
		self.assertEqual([1], sort([1]))
		self.assertEqual([], sort([]))

if __name__ == '__main__':
	unittest.main()