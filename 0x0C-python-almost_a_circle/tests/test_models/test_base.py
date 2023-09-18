#!/usr/bin/python3
import unittest

from models.base import Base
from models.rectangle import Rectangle
from pathlib import Path


class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0
        self.b1 = Base()
        self.b2 = Base(-3)
        self.b3 = Base(7)
        self.b4 = Base()

    def tearDown(self):
        pass

    def test_id(self):
        print()
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, -3)
        self.assertEqual(self.b3.id, 7)
        self.assertEqual(self.b4.id, 2)

        b6 = Base("l")
        self.assertEqual(b6.id, "l")

    def test_objects(self):
        # print(f"k {Base.__nb_objects}")
        self.assertEqual(Base._Base__nb_objects, 2)
        b5 = Base(3)
        self.assertEqual(b5.id, 3)
        b6 = Base()
        self.assertEqual(b6.id, 3)
        self.assertEqual(Base._Base__nb_objects, 3)

    def test_to_json_string(self):

        self.assertEqual(
            Base.to_json_string([{"id": 2,
                                  "height": 5, "width": 4}]),
            '[{"id": 2, "height": 5, "width": 4}]')
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        with self.assertRaises(TypeError):
            Base.to_json_string("l")
        with self.assertRaises(TypeError):
            Base.to_json_string([{"id": 90}, "o"])

    def test_from_json_string(self):
        lis = Base.to_json_string([{'height': 4, 'width': 10, 'id': 89},
                                   {'height': 7, 'width': 1, 'id': 7}])
        self.assertEqual(Base.from_json_string(lis),
                         [{"height": 4, "width": 10, "id": 89},
                          {"height": 7, "width": 1, "id": 7}])

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

        with self.assertRaises(TypeError):
            Base.from_json_string([])

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        self.assertTrue(Path.exists(Path("Rectangle.json")))

        with open("Rectangle.json", "r", encoding="UTF8") as fp:
            self.assertTrue(isinstance(fp.read(), str))

        with self.assertRaises(TypeError):
            Rectangle.save_to_file("")
