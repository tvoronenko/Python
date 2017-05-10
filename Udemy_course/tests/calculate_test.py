import unittest
from app.calculate import Calculate

class TestCalculate(unittest.TestCase):
	def setUp(self):
		self.calc = Calculate()

	def test_add_method_returns_correct_result(self):
		self.assertEquals(4, self.calc.add(2, 2))

	def test_add_method_returns_incorrect_result(self):
		self.assertEquals(4, self.calc.add(2, 3))
	
	def test_add_method_raises_typerror_if_not_inits(self):
		self.assertRaises(TypeError, self.calc.add, "Hello", "World")

if __name__ == '__main__':
	unittest.main()