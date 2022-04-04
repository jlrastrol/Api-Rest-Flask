import unittest
from module_operations.operations import operations
class TestOperations(unittest.TestCase):

    def setUp(self):
        self.a = [6,5,9,8]
        self.b = [2,5,2,2]
        self.oper = operations()

    def test_suma(self):
        '''
        Test that verifies that the value of the sum operation is correct.
        '''
        valorCalculado = operations.suma(self.oper,self.a,self.b)
        valorReal = [8, 10, 11, 10]
        self.assertEqual(valorCalculado, valorReal)
    
    def test_suma_int(self):
        '''
        Test that verifies that the type of the input parameters is list.
        '''
        self.assertRaises(TypeError, operations.suma,self.oper, 4,7)
    
    def test_suma_list_not_int(self):
        '''
        Test that verifies that the data type of the input parameters are numbers.
        '''
        listDistinct = ["1",3,"a"]
        self.assertRaises(TypeError, operations.suma,self.oper, self.a, listDistinct)

    def test_suma_distinct_size_list(self):
        '''
        Test that verifies that the size of the input parameters is equal.
        '''
        listDistinct = [2,3,4]
        self.assertRaises(OverflowError, operations.suma, self.oper, self.a, listDistinct)

    def test_resta(self):
        '''
        Test that verifies that the value of the subtraction operation is correct.        
        '''
        valorCalculado = operations.resta(self.oper,self.a,self.b)
        valorReal = [4, 0, 7, 6]
        self.assertEqual(valorCalculado, valorReal)

    def test_resta_int(self):
        '''
        Test that verifies that the type of the input parameters is list.
        '''
        self.assertRaises(TypeError, operations.resta,self.oper, 4,7)

    def test_resta_list_not_int(self):
        '''
        Test that verifies that the data type of the input parameters are numbers.
        '''
        listDistinct = ["1",3,"a"]
        self.assertRaises(TypeError, operations.resta,self.oper, self.a, listDistinct)
    
    def test_resta_distinct_size_list(self):
        '''
        Test that verifies that the size of the input parameters is equal.
        '''
        listDistinct = [2,3,4]
        self.assertRaises(OverflowError, operations.resta,self.oper, self.a,listDistinct)

    def test_mult(self):
        '''
        Test that verifies that the value of the multiplication operation is correct.        
        '''
        valorCalculado = operations.mult(self.oper,self.a,self.b)
        valorReal = [12, 25, 18, 16]
        self.assertEqual(valorCalculado, valorReal)

    def test_mult_int(self):
        '''
        Test that verifies that the type of the input parameters is list.
        '''
        self.assertRaises(TypeError, operations.mult,self.oper, 4,7)

    def test_mult_list_not_int(self):
        '''
        Test that verifies that the data type of the input parameters are numbers.
        '''
        listDistinct = ["1",3,"a"]
        self.assertRaises(TypeError, operations.mult,self.oper, self.a, listDistinct)

    def test_mult_distinct_size_list(self):
        '''
        Test that verifies that the size of the input parameters is equal.
        '''
        listDistinct = [2,3,4]
        self.assertRaises(OverflowError, operations.mult,self.oper, self.a, listDistinct)

    def test_divis(self):
        '''
        Test that verifies that the value of the division operation is correct.        
        '''
        valorCalculado = operations.divis(self.oper, self.a,self.b)
        valorReal = [3, 1, 4.5, 4]
        self.assertEqual(valorCalculado, valorReal)

    def test_divis_int(self):
        '''
        Test that verifies that the type of the input parameters is list.
        '''
        self.assertRaises(TypeError, operations.divis, 4,7)

    def test_divis_list_not_int(self):
        '''
        Test that verifies that the data type of the input parameters are numbers.
        '''
        listDistinct = ["1",3,"a"]
        self.assertRaises(TypeError, operations.divis,self.oper, self.a, listDistinct)

    def test_divis_distinct_size_list(self):
        '''
        Test that verifies that the size of the input parameters is equal.
        '''
        listDistinct = [2,3,4]
        self.assertRaises(OverflowError, operations.divis, self.oper, self.a,listDistinct)

    def test_divisBy0(self):
        '''
        Test that verifies that a division by 0 cannot be performed.
        '''
        self.b = [2,5,0,2]
        self.assertRaises(ZeroDivisionError, operations.divis, self.oper, self.a,self.b)

if __name__ == "__main__":
    unittest.main()