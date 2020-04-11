import unittest
from Student import Student

class Test_Staff(unittest.TestCase):

    def setUp(self):
        """instantiate the class in every method"""
        self.student1 = Student(1,"Mike","Liao",50,50000,["python","web"])

    def test_init(self):
        """010A"""
        self.assertTrue(self.student1._tuition == 50000)
        self.assertTrue(self.student1._courses == ["python","web"])

    def test_get_tuition(self):
        """040A"""
        self.assertTrue(self.student1.get_tuition() == 50000)

    def test_get_courses(self):
        """050A"""
        self.assertTrue(self.student1.get_courses() == ["python","web"])

    def test_to_dict(self):
        self.assertTrue(self.student1.to_dict()["id"] == 1)
        self.assertTrue(self.student1.to_dict()["fname"] == "Mike")
        self.assertTrue(self.student1.to_dict()["lname"] == "Liao")
        self.assertTrue(self.student1.to_dict()["age"] == 50)
        self.assertTrue(self.student1.to_dict()["tuition"] == 50000)
        self.assertTrue(self.student1.to_dict()["courses"] == ["python","web"])
