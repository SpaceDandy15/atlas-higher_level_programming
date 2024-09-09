#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = 
max_intege
__import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    
"""Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [
        ordered =

        orde
1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 
        self.assertEqual(max_integer(ordere

        self.assertEqual(
        se

     
4)

    def test_unordered_list(self):
        
     
"""Test an unordered list of integers."""
        unordered = [
        unor
1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 
        self.assertEqual(max_integer(unorder

        
4)

    

 
def test_max_at_beginning(self):
        
    
"""Test a list with a beginning max value."""
        max_at_beginning = [
        max_at_beginnin

     
4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 
        self.assertEqual(max_integer(max_at

        self.assertEqual(max_i

        self.asse

        sel
4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), 
        empty = []
        self.assertEqual(max_integer(e

        empty = []
        self.assertEqual(

        empty = []
        self.asser

        empty = []
        sel

        empty = []
   

        empty
None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [
        one_eleme

  
7]
        self.assertEqual(max_integer(one_element), 
        self.assertEqual(max_integer(one_element), 

        self.asse

    
7)

    def test_floats(self):
        
   
"""Test a list of floats."""
        floats = [
        floats = 

     
1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 
        self.assertEqual(max_integer(floats

        self.assertEqual(max_integer(flo

        self.assertEqual(max_in

        self.assertEqual(
        self.assertEqual(

        self.assertEqu

        self.ass

        

    
15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [
        ints_and_floats =

        ints

      
1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 
        self.assertEqual(max_integer(ints_and_floats)

        self.assertEqual(max_

        self.a

      

  
15.5)

    def test_string(self):
        
        
"""Test a string."""
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        
   
"""Test a list of strings."""
        strings = [
        strings 

        strin

       

    
"Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), 
        self.assertEqual(max_integer(s

        self.assertEqual(max_

        self.assertEq

       
"name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(
        self.assertEqual(
""), None)

if __name__ == '__main__':
    unittest.main()

