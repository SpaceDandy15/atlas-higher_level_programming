import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_dict(self):
        dicts = [{'id': 1, 'width': 10}]
        self.assertEqual(Base.to_json_string(dicts), '[{"id": 1, "width": 10}]')

    def test_save_to_file(self):
        r = Rectangle(10, 7, 2, 3)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", 'r') as file:
            self.assertEqual(file.read(), '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 3}]')

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string(self):
        json_string = '[{"id": 1, "width": 10}]'
        self.assertEqual(Base.from_json_string(json_string), [{'id': 1, 'width': 10}])

    def test_create_rectangle(self):
        r = Rectangle.create(**{'id': 1, 'width': 10, 'height': 7})
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 7)

    def test_load_from_file(self):
        r = Rectangle(10, 7, 2, 3)
        Rectangle.save_to_file([r])
        r_list = Rectangle.load_from_file()
        self.assertEqual(len(r_list), 1)
        self.assertEqual(r_list[0].id, 1)

if __name__ == "__main__":
    unittest.main()
