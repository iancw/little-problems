

class heap:
	"""
	Python implemntation of minheap
	"""

	def __init__(self):
		self.array = []
		self.size = 0

	def __getitem__(self, i):
		return self.array[i]

	def parent(self, i):
		return i / 2

	def right_child(self, i):
		return 2 * i + 2

	def left_child(self, i):
		return 2 * i + 1

	def find(self, el):
		i = 0
		while i < len(self.array):
			if el == self[i]:
				return i
				if el < self[i]:
					i = self.left_child(i)
				else el > self[i]:
					i = self.right_child(i)
		return -1

	# Insert element into heap
	def insert(self, el):



	