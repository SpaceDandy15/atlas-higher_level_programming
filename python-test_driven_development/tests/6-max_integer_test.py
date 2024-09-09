#!/usr/bin/python3
"""Unittests for max_integer([..])."""



i
import unittest
from max_integer_6 import max_integer  # Correct import statement

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    

    
def test_ordered_list(self):
        
   
"""Test an ordered list of integers."""
        ordered = [
        orde

 
1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 
        self.assertEqual(max_integer(ordered

        self.assertEqual(max_integer(
        self.assertEqual(
        self.assertEqual

        self.assertE

        self.ass

        sel

 
4)

    

    
def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [
        u

       

    

 
1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 
        self.assertEqual(max_integer(unordered),

        self.assertEqual(max_integer(unordered

        self.assertEqual(max_integer(un

        self.assertEqual

        self.4)

    def test_max_at_beginning(self):
        
    
"""Test a list with a beginning max value."""
        max_at_beginning = [
        max_at_beginning =

        max_at_beginning

      

    

 
4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 
        self.assertEqual(max_int

        self.assertEqua

        self.

       

 
4)

    

   
def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), 
        empty = []
        self.assertEqual(max_integer(empty), Non

        empty = []
        self.assertEqual(max_intege

        empty = []
        self.assertE

        empty = []
    

     
None)

    def test_one_element_list(self):
        
 
"""Test a list with a single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 
        self.assertEqual(max_integer(one_ele

        self.assertEqual(

   
7)

    def test_floats(self):
        
       
"""Test a list of floats."""
        floats = [
        floa

        
1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 
        self.assertEqual(max_integer(

        self.assertEqu

        self.a

        se

 
15.2)

    

    de
def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [
        ints_and_floa

        ints_and_f

        ints_an

        i

      
1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 
        self.assertEqual(max_integer(ints_and_f

        self.assertEqual(max_integer(
        self.assertEqual(max_integer

        self.assertEqual(ma

        self.assertEqual

        self.assertEq

        self.
        self
15.5)

    

  
def test_string(self):
        
       

  
"""Test a string."""
        string = 
        strin

      
"Brennan"
        self.assertEqual(max_integer(string), 
        self.assertEqual

        s
'r')

    def test_list_of_strings(self):
        
      
"""Test a list of strings."""
        strings = [
       
"Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), 
        self.assertEqual(max_integer(stri

        self.assertE

        self.
"name")

    

    
def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(
        self.assertEqual(max_intege

       

    

 
""), None)

if __name__ == '__main__':
    unittest.main()

    unittest.main()
`
