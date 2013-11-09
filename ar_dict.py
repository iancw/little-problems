
class ar_dict:
	"""
	Python implemntation of dictionary using unsorted arrays
	"""

        def __init__(self):
          self.size = 0
          self.keys = []
          self.values = []

        def find_idx(self, key):
          """
          Find index of key, runs in O(n) time
          """
          for i in range(0, self.size):
            if self.keys[i] == key:
              return i
          return None

        def insert(self, key, value):
          """
          Insert key, value pair, runs in O(n) time 
          because of find_idx call to search for existing
          entries.
          """
          existing = self.find_idx(key)
          if existing is None:
            self.keys.append(key)
            self.values.append(value)
          else:
            self.values[existing] = value
          self.size += 1

        def get(self, key):
          """
          Retrieve value for key, O(n)
          """
          idx = self.find_idx(key)
          if idx is None:
            return None
          return self.values[idx]

        def delete(self, key):
          """
          Remove key, value pair if they exist, runs in O(n) time
          """
          idx = self.find_idx(key)
          if idx is None:
            return None
          # Swap tail value into now empty slot, decrease size by 1
          self.keys[idx] = self.keys[self.size-1]
          self.values[idx] = self.values[self.size-1]
          self.size -= 1

