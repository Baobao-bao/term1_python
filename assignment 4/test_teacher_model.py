from peewee import SqliteDatabase
from teacher_model import Teacher_m
import unittest
db = SqliteDatabase("school.sqlite")
db.connect()

class Test_Teacher_m(unittest.TestCase):
    def setUp(self):
        """instantiate the class in every method"""
        self.tea1 = Teacher_m(id=3, fname="Mike", lname="Liao", age=18, salary=10000,courses="math")
        self.tea1.save()

    def test_to_dict(self):
        self.assertTrue(self.tea1.to_dict()["id"] == 3)
        self.assertTrue(self.tea1.to_dict()["fname"] == "Mike")
        self.assertTrue(self.tea1.to_dict()["lname"] == "Liao")
        self.assertTrue(self.tea1.to_dict()["age"] == 18)
        self.assertTrue(self.tea1.to_dict()["salary"] == 10000)
        self.assertTrue(self.tea1.to_dict()["courses"] == "math")

    def test_post(self):
        self.tea1.post()
        self.assertTrue(Teacher_m.get(Teacher_m.id == 3))

