import unittest
from no_fours import brute, fast

class TestNoFours(unittest.TestCase):

	def test(self):
	    for n in range(0, 40000):
	        b=brute(n)
	        f=fast(n)
	        self.assertEqual(b, f, 'for n=%d brute=%d, fast=%d' % (n,b,f))

if __name__ == '__main__':
	unittest.main()