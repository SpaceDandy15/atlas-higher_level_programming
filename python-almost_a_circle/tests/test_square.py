import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_initialization(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_invalid_size(self):
        with self.assertRaises(ValueError):
            s = Square(0)

    # Add more tests...

if __name__ == '__main__':
    unittest.main()
