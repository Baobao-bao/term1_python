import unittest
from Staff import Staff

class Test_Staff(unittest.TestCase):

    def setUp(self):
        """instantiate the class in every method"""
        self.staff1 = Staff(1,"Mike","Liao",50,50000,"cleaner")

    def test_init(self):
        """010A"""
        self.assertTrue(self.staff1._salary == 50000)
        self.assertTrue(self.staff1._position == "cleaner")

    def test_get_salary(self):
        """040A"""
        self.assertTrue(self.staff1.get_salary() == 50000)

    def test_get_position(self):
        """050A"""
        self.assertTrue(self.staff1.get_position() == "cleaner")

    def test_to_dict(self):
        self.assertTrue(self.staff1.to_dict()["id"] == 1)
        self.assertTrue(self.staff1.to_dict()["fname"] == "Mike")
        self.assertTrue(self.staff1.to_dict()["lname"] == "Liao")
        self.assertTrue(self.staff1.to_dict()["age"] == 50)
        self.assertTrue(self.staff1.to_dict()["salary"] == 50000)
        self.assertTrue(self.staff1.to_dict()["position"] == "cleaner")