
class my_hash:
	"""
	Python implemntation of hash map using unsorted arrays
	"""

        def __init__(self):
          self.size = 0
          self.keys = []
          self.values = []

        def find_idx(self, key):
          for i in range(0, len(self.keys)):
            if self.keys[i] == key:
              return i
          return None

        def insert(self, key, value):
          existing = self.find_idx(key)
          if existing is None:
            self.keys.append(key)
            self.values.append(value)
          else:
            self.values[existing] = value
          self.size += 1

        def get(self, key):
          idx = self.find_idx(key)
          if idx is None:
            return None
          return self.values[idx]

        def delete(self, key):
          idx = self.find_idx(key)
          if idx is None:
            return None
          # Swap tail value into now empty slot, decrease size by 1
          self.keys[idx] = self.keys[self.size-1]
          self.values[idx] = self.values[self.size-1]
          self.size -= 1

