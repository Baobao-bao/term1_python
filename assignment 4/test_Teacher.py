import unittest
from Teacher import Teacher

class Test_Staff(unittest.TestCase):

    def setUp(self):
        """instantiate the class in every method"""
        self.teacher1 = Teacher(1,"Mike","Liao",50,80000,["python","web"])

    def test_init(self):
        """010A"""
        self.assertTrue(self.teacher1._salary == 80000)
        self.assertTrue(self.teacher1._courses == ["python","web"])

    def test_get_salary(self):
        """040A"""
        self.assertTrue(self.teacher1.get_salary() == 80000)

    def test_get_courses(self):
        """050A"""
        self.assertTrue(self.teacher1.get_courses() == ["python","web"])

    def test_to_dict(self):
        self.assertTrue(self.teacher1.to_dict()["id"] == 1)
        self.assertTrue(self.teacher1.to_dict()["fname"] == "Mike")
        self.assertTrue(self.teacher1.to_dict()["lname"] == "Liao")
        self.assertTrue(self.teacher1.to_dict()["age"] == 50)
        self.assertTrue(self.teacher1.to_dict()["salary"] == 80000)
        self.assertTrue(self.teacher1.to_dict()["courses"] == ["python","web"])





