
class heap:
  """
  Python implemntation of minheap
  """

  def __init__(self, ar=[]):
    self.array = ar
    self.size = 0
    for i in range(0, len(ar)):
      self.insert(ar[i])

  def __getitem__(self, i):
    return self.array[i]

  def parent(self, i):
    if i == 0:
      return -1
    return (i-1) / 2

  def right_child(self, i):
    return 2 * i + 2

  def left_child(self, i):
    return 2 * i + 1

  def swap(self, i, j):
    t = self.array[i]
    self.array[i] = self.array[j]
    self.array[j] = t

  def extract_min(self):
    m = self.array[0]
    self.swap(0, self.size - 1)
    self.size -= 1
    self.array[self.size] = -1
    self.heapify_down(0)
    return m

  def heapify_up(self, node):
    """
    Recursively compares node at index node to parent
    and swaps until parent is less than node
    """
    if node == 0:
      return
    p = self.parent(node)
    if self[node] < self[p]:
      self.swap(node, p)
      self.heapify_up(p)

  def heapify_down(self, node):
    """
    Compares node to its two children, if node violates
    min heap constraint (that is, if node is greater than
    either of its children) then the node is swapped
    with its min child and the method is called recursively
    """
    l = self.left_child(node)
    r = self.right_child(node)
    m = l
    if r < self.size and self[r] < self[l]:
      m = r
    if m < self.size and self[m] < self[node]:
      self.swap(m, node)
      self.heapify_down(m)

  def find(self, el):
    i = 0
    while i < len(self.array):
      if el == self[i]:
        return i
        if el < self[i]:
          i = self.left_child(i)
        else: # el > self[i]:
          i = self.right_child(i)
    return -1

  # Insert element into heap
  def insert(self, el):
    if self.size == len(self.array):
      print "appending %d" % el
      self.array.append(el)
    else:
      print "inserting %d" % el
      self.array[self.size] = el
    print "new array is %s" % self.array
    self.heapify_up(self.size )
    self.size += 1
