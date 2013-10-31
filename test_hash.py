import unittest
from my_hash import my_hash

class TestHeap(unittest.TestCase):

  def test_hash(self):
    h = my_hash()
    h.insert("hash", 1)
    self.assertEqual(1, h.get("hash"))

  def test_overwrite(self):
    h = my_hash()
    h.insert("hash", 1)
    h.insert("hash", 2)
    self.assertEqual(2, h.get("hash"))

  def test_delete(self):
    h = my_hash()
    h.insert("hashyhash", 1)
    self.assertEquals(1, h.get("hashyhash"))
    h.delete("hashyhash")
    self.assertEquals(None, h.get("hashyhash"))


if __name__ == '__main__':
  unittest.main()

