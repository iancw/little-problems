import unittest
from bin_tree import BinTree

class TestTree(unittest.TestCase):

  def test_basic(self):
    b = BinTree()
    b.insert(2)
    self.assertEquals(1,b.size())
    self.assertEquals(1, b.depth())
    b.insert(1)
    self.assertEquals(2, b.size())
    self.assertEquals(2, b.depth())
    b.insert(3)
    self.assertEquals(3, b.size())
    self.assertEquals(2, b.depth())
  def test_unbalanced(self):
    b = BinTree()
    b.insert(1)
    self.assertEquals(1, b.depth())
    b.insert(2)
    self.assertEquals(2, b.depth())
    b.insert(3)
    self.assertEquals(3, b.depth())

if __name__ == '__main__':
  unittest.main();

