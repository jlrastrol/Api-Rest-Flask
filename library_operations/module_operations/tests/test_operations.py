
import unittest
from module_operations.operations import *

class TestOperations(unittest.TestCase):

    def setUp(self):
        self.a = [6,5,9,8]
        self.b = [2,5,2,2]

    def test_suma(self):
        valorCalculado = suma(self.a,self.b)
        valorReal = [8, 10, 11, 10]
        self.assertEqual(valorCalculado, valorReal)
    
    def test_suma_int(self):
        self.assertRaises(TypeError, sum, 4,7)

    def test_suma_distinct_size_list(self):
        listDistinct = [2,3,4]
        self.assertRaises(OverflowError, suma, self.a, listDistinct)

    def test_resta(self):
        valorCalculado = resta(self.a,self.b)
        valorReal = [4, 0, 7, 6]
        self.assertEqual(valorCalculado, valorReal)

    def test_resta_int(self):
        self.assertRaises(TypeError, resta, 4,7)
    
    def test_resta_distinct_size_list(self):
        listDistinct = [2,3,4]
        self.assertRaises(OverflowError, resta, self.a,listDistinct)

    def test_mult(self):
        valorCalculado = mult(self.a,self.b)
        valorReal = [12, 25, 18, 16]
        self.assertEqual(valorCalculado, valorReal)

    def test_mult_int(self):
        self.assertRaises(TypeError, mult, 4,7)

    def test_mult_distinct_size_list(self):
        listDistinct = [2,3,4]
        self.assertRaises(OverflowError, mult, self.a, listDistinct)

    def test_divis(self):
        valorCalculado = divis(self.a,self.b)
        valorReal = [3, 1, 4.5, 4]
        self.assertEqual(valorCalculado, valorReal)

    def test_divis_int(self):
        self.assertRaises(TypeError, divis, 4,7)

    def test_divis_distinct_size_list(self):
        listDistinct = [2,3,4]
        self.assertRaises(OverflowError, divis, self.a,listDistinct)

    def test_divisBy0(self):
        self.b = [2,5,0,2]
        self.assertRaises(ZeroDivisionError, divis, self.a,self.b)

if __name__ == "__main__":
    unittest.main()