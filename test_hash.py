import unittest
from my_hash import my_hash

class TestHeap(unittest.TestCase):

  def test_hash(self):
    h = my_hash(10)
    h.insert("hash", 1)
    self.assertEqual(1, h.get("hash"))

  def test_overwrite(self):
    h = my_hash(10)
    h.insert("hash", 1)
    h.insert("hash", 2)
    self.assertEqual(2, h.get("hash"))

  def test_delete(self):
    h = my_hash(10)
    h.insert("hashyhash", 1)
    self.assertEquals(1, h.get("hashyhash"))
    h.delete("hashyhash")
    self.assertEquals(None, h.get("hashyhash"))

  def test_chaining(self):
    h = my_hash(10)
    # Cases hand-picked to present collisions
    h.insert('hash16', 16) # hashes to index 7
    h.insert('hash18', 18) # also hashes to index 7
    self.assertEquals(18, h.get('hash18'))
    self.assertEquals(16, h.get('hash16'))

if __name__ == '__main__':
  unittest.main()

