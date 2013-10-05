import unittest
from heap import heap

class TestHeap(unittest.TestCase):

	def test_heap(self):
		h = heap()
		h.insert(1)


if __name__ == '__main__':
	unittest.main()