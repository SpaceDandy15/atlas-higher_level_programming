import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_initialization(self):
        r = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_to_dictionary(self):
        r = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(r.to_dictionary(), {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3})

    def test_update_with_kwargs(self):
        r = Rectangle(5, 10)
        r.update(id=3, width=6, height=12)
        self.assertEqual(r.id, 3)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 12)

    def test_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        r = Rectangle(5, 3, 1, 1)
        # Use StringIO to capture printed output
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "\n #####\n #####\n #####\n")

if __name__ == "__main__":
    unittest.main()
