import unittest
from School import School
from Person import Person

class Test_School(unittest.TestCase):

    def setUp(self):
        """instantiate the class in every method"""
        self.school1 = School("bcit","Seymour Street 555,Vancouver")
        self.person1  = Person(1,"Mike","Liao",80)

    def test_init(self):
        """010A"""
        self.assertTrue(self.school1._name == "bcit")
        self.assertTrue(self.school1._address == "Seymour Street 555,Vancouver")
        self.assertTrue(self.school1._people == [])

        
    def test_add_person(self):
        """030A"""
        self.assertTrue(len(self.school1._people) == 0)
        self.school1.add_person(self.person1)
        self.assertTrue(len(self.school1._people) == 1)

    def test_del_person(self):
        """030B"""
        self.school1.add_person(self.person1)
        self.assertTrue(len(self.school1._people) == 1)
        self.school1.del_person(1)
        self.assertTrue(len(self.school1._people) == 0)

    def test_get_all_by_firstname(self):
        """030C"""
        self.school1.add_person(self.person1)
        self.assertTrue(self.school1.get_all_by_firstname("Mike")[0]._fname == "Mike")




