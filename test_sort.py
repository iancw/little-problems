import unittest
from no_fours import brute, fast
from sort import heapsort, mergesort, quicksort
import time
import random

class TestSort(unittest.TestCase):

	def test_heap(self):
		self.help_sort(heapsort)

	def test_quick(self):
		self.help_sort(quicksort)

	def test_merge(self):
		self.help_sort(mergesort)

	def help_sort(self, sort):
		start = time.clock()
		self.assertEqual([1,2,3,5,7,9], sort([1, 5, 2, 9, 3, 7]))
		self.assertEqual([1,2,3,7,9], sort([1, 2, 3, 7, 9]))
		self.assertEqual(range(0, 10), sort(range(0,10)[::-1]))
		self.assertEqual([1], sort([1]))
		self.assertEqual([], sort([]))
		ar = [int(100000*random.random()) for i in xrange(100000)]
		sorted_ar = sort(ar)
		for i in range(0, len(ar)-1):
			self.assertTrue(sorted_ar[i] <= sorted_ar[i+1])
		# Test the pathological case for quicksort
		self.assertEqual(range(0, 10000), sort(range(0, 10000)))
		self.assertEqual(range(0, 10000), sort(range(0, 10000)[::-1]))
		end = time.clock()
		print "%s ran in %f seconds" % (sort, (end-start))

if __name__ == '__main__':
	unittest.main()