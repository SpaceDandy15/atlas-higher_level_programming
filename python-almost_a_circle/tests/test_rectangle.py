import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_initialization(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)

    def test_invalid_width(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 10)

    # Add more tests...

if __name__ == '__main__':
    unittest.main()
