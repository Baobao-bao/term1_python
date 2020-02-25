import unittest
from Person import Person
from datetime import *
class Test_Person(unittest.TestCase):

    def setUp(self):
        self.person1 = Person(1,"Mike","Liao",80)

    def test_init(self):
        self.assertTrue(self.person1._id == 1)
        self.assertTrue(self.person1._fname == "Mike")
        self.assertTrue(self.person1._lname == "Liao")
        self.assertTrue(self.person1._age == 80)
        self.assertTrue(self.person1.get_datestart() == date.today())

    def test_get_id(self):
        self.assertTrue(self.person1.get_id() == 1)

    def test_get_fname(self):
        self.assertTrue(self.person1.get_fname() == "Mike")

    def test_get_lname(self):
        self.assertTrue(self.person1.get_lname() == "Liao")

    def test_get_age(self):
        self.assertTrue(self.person1.get_age() == 80)

    def test_get_datastart(self):
        self.assertTrue(self.person1.get_datestart() == date.today())


