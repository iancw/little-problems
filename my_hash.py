class my_hash:
  """
  Implementation of hash map, uses open addressing for conflict
  resolution
  """

  def __init__(self, size):
    self.size = size
    self.data = [None] * size

  def __hash(self, key):
    """
      Simple hash
    """
    return 0


  def insert(self, key, value):
    """
    Insert key, value pair, runs in O(1) time 
    """
    idx = self.__hash(key)
    for i in range(idx, self.size):
      if self.data[i] is None:
        self.data[i] = value
        return
    # Continue the search by wrapping if necesary
    for i in range(0, idx):
      if self.data[i] is None:
        self.data[i] = value
        return
    raise Exception("No space left in the array")


