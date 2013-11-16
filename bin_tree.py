class BinNode:
  def __init__(self, value):
    self.value = value
    self.parent = None
    self.left = None
    self.right = None

class BinTree:

  def __init__(self):
    self.root = None

  def depth(self):
    return self.__rec_depth(self.root)

  def __rec_depth(self, node):
    if node is None:
      return 0
    return 1 + max(self.__rec_depth(node.left), self.__rec_depth(node.right))

  def size(self):
    return self.rec_count(self.root)

  def rec_count(self, node):
    if node is None:
      return 0
    return self.rec_count(node.left) + 1 + self.rec_count(node.right)

  def print_tree(self):
    self.__rec_print(self.root)

  def __rec_print(self, node):
    if node is None:
      return
    self.__rec_print(node.left)
    print "%s: [%s, %s]" % (repr(node.value), repr(node.left), repr(node.right))
    self.__rec_print(node.right)

  def insert(self, value):
    (node, parent) = self.search(value)
    new_node = BinNode(value)
    new_node.parent = parent
    if self.root is None:
      self.root = new_node
      return
    if parent.value == value:
      print 'Value %s is already in tree' % value
      return
    if parent is None:
      print "Error, parent should not be None if self.root is not None"
    if node is not None:
      print "Error, node is not none"
    if value < parent.value:
      if parent.left is not None:
        print "wowza errors parent left"
      parent.left = new_node
    else:
      if parent.right is not None:
        print "wowza errors parent right"
      parent.right = new_node

  def search(self, value):
    cur = self.root
    parent = None
    while cur is not None:
      if cur.value == value:
        return (cur, parent)
      parent = cur
      if value < cur.value:
        cur = cur.left
      else:
        cur = cur.right
    return (cur, parent)

