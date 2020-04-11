from peewee import SqliteDatabase
from staff_model import Staff_m
import unittest
db = SqliteDatabase("school.sqlite")
db.connect()

class Test_Staff_m(unittest.TestCase):
    def setUp(self):
        """instantiate the class in every method"""
        self.sta1 = Staff_m(id=2, fname="Mike", lname="Liao", age=18, salary=10000,position="cleaner")
        self.sta1.save()

    def test_to_dict(self):
        self.assertTrue(self.sta1.to_dict()["id"] == 2)
        self.assertTrue(self.sta1.to_dict()["fname"] == "Mike")
        self.assertTrue(self.sta1.to_dict()["lname"] == "Liao")
        self.assertTrue(self.sta1.to_dict()["age"] == 18)
        self.assertTrue(self.sta1.to_dict()["salary"] == 10000)
        self.assertTrue(self.sta1.to_dict()["position"] == "cleaner")

    def test_post(self):
        self.sta1.post()
        self.assertTrue(Staff_m.get(Staff_m.id == 2))

