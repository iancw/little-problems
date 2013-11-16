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
    h_idx = hash(key) % self.size
    print "Hashed %s to %d" %(key, h_idx)
    return h_idx

  def get(self, key):
    idx = self.__hash(key)
    if self.data[idx] is None:
      return None
    for i in range(idx, self.size):
      if self.data[i] is None:
        return None
      if  self.data[i][0] == key:
        return self.data[i][1]
    for i in range(0, idx):
      if self.data[i] is None:
        return None
      if  self.data[i][0] == key:
        return self.data[i][1]
    return None


  def delete(self, key):
    idx = self.__hash(key)
    if self.data[idx] is None:
      return None
    old_data = self.data[idx]
    self.data[idx] = None
    return old_data[1]

  def insert(self, key, value):
    """
    Insert key, value pair, runs in O(1) time 
    """
    idx = self.__hash(key)
    for i in range(idx, self.size):
      if self.data[i] is not None:
        print "Chaining for key %s, conflicts with key %s!" % (key, self.data[i][0])
      if (self.data[i] is None) or (self.data[i][0] == key):
        self.data[i] = (key, value)
        print "Finally put %s at %d" % (key, i)
        print self.data
        return
    # Continue the search by wrapping if necesary
    for i in range(0, idx):
      if self.data[i] is None or (self.data[i][0] == key):
        self.data[i] = (key, value)
        print "Finally put %s at %d" % (key, i)
        print self.data
        return
    raise Exception("No space left in the array")


