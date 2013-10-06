import unittest
from heap import heap

class TestHeap(unittest.TestCase):

	def test_heap(self):
		h = heap()
		h.insert(1)
		self.assertEqual(1, h.extract_min())

	def test_two(self):
		h = heap()
		h.insert(2)
		h.insert(1)
		self.assertEqual(1, h.extract_min())
		self.assertEqual(2, h.extract_min())

	def test_internals(self):
		h = heap()
		h.insert(5)
		h.insert(4)
		h.insert(3)		
		h.insert(2)
		self.assertEquals(-1, h.parent(0))
		self.assertEquals(0, h.parent(1))
		self.assertEquals(0, h.parent(2))
		self.assertEquals(1, h.left_child(0))
		self.assertEquals(2, h.right_child(0))
		self.assertEquals(3, h.left_child(1))
		self.assertEquals(4, h.right_child(1))		
		self.assertEquals(5, h.left_child(2))
		self.assertEquals(6, h.right_child(2))
		self.assertEquals(2, h.parent(6))

	def test_larger(self):
		h = heap()
		for i in range(10, 0, -1):
			h.insert(i)

		for i in range(1, 11):
			self.assertEquals(i, h.extract_min())

if __name__ == '__main__':
	unittest.main()