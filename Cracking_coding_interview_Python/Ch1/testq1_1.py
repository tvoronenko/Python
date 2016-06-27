import unittest
from q1_1 import *

class ExpectedResult(unittest.TestCase):
	def testEmptyStr(self):
		'must return True'
		result = isUniqueChars('')
		self.assertTrue(result)
		
if __name__ == '__main__':
    unittest.main()