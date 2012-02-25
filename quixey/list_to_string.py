import unittest
"""
Author: Eric Gustavson

Problem Statement: 

Implement a function similar to str() or repr() as follows:
	
  Precondition: input is a list-only data structure
  Output: a string of the corresponding list literal
  
  Example:
  [[], [[], []]] -> '[[], [[], []]]'

"""

class Converter:

    def __init__(self):
        self.s = ''

    def list_to_str(self, l):
        if not isinstance(l, list):
            raise TypeError("Expected a list, but got " + str(type(l))) 
        self.s += '['
        for n, i in enumerate(l):
            self.list_to_str(i)
            if not len(l) - 1 == n:
                self.s += ', '
        self.s += ']'
        return self.s

class ConvertTest(unittest.TestCase):
    def setUp(self):
        self.c = Converter()

    def test_empty_string(self):
        l = ''
        self.assertRaises(TypeError, self.c.list_to_str, l)
        
    def test_none(self):
        l = None
        self.assertRaises(TypeError, self.c.list_to_str, l)
        
    def test_empty_list(self):
        l = []
        self.assertEqual(self.c.list_to_str(l), str(l))
        
    def test_long_list(self):
        l = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
        self.assertEqual(self.c.list_to_str(l), str(l))
    
    def test_nested_beast(self):    
        l = [[[[[[[[[[[[[],[],[],[[[[[[[[]]]]]]]],[],[]]]]]]]]]]]],[],[],[],[],[],[],[[[],[],[],[],[],[[[[[[[[],[[[[[]]]]]]]]]]]],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]],[],[],[],[],[],[],[],[],[],[],[],[]]
        self.assertEqual(self.c.list_to_str(l), str(l))

if __name__ == '__main__':
    unittest.main()
