from peewee import SqliteDatabase
from student_model import Student_m
import unittest
db = SqliteDatabase("school.sqlite")
db.connect()

class Test_Student_m(unittest.TestCase):
    def setUp(self):
        """instantiate the class in every method"""
        self.stu1 = Student_m(id=1, fname="Mike", lname="Liao", age=18, tuition=10000,courses="math")
        self.stu1.save()

    # def test_to_dict(self):
    #     self.assertTrue(self.stu1.to_dict()["id"] == 1)
    #     self.assertTrue(self.stu1.to_dict()["fname"] == "Mike")
    #     self.assertTrue(self.stu1.to_dict()["lname"] == "Liao")
    #     self.assertTrue(self.stu1.to_dict()["age"] == 50)
    #     self.assertTrue(self.stu1.to_dict()["tuition"] == 50000)
    #     self.assertTrue(self.stu1.to_dict()["courses"] == ["python","web"])

    # def test_post(self):
    #     self.stu1.post()
    #     self.assertTrue(Student_m.get(Student_m.id == 1))

