import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_initialization(self):
        s = Square(5, 2, 3, 1)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_to_dictionary(self):
        s = Square(5, 2, 3, 1)
        self.assertEqual(s.to_dictionary(), {'id': 1, 'size': 5, 'x': 2, 'y': 3})

    def test_update_with_kwargs(self):
        s = Square(5)
        s.update(id=3, size=10, x=1, y=0)
        self.assertEqual(s.id, 3)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 0)

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_display(self):
        s = Square(5, 2, 3)
        # Use StringIO to capture printed output
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "\n\n  #####\n  #####\n  #####\n  #####\n  #####\n")

if __name__ == "__main__":
    unittest.main()
