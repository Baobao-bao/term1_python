from Staff import Staff
from Student import Student
from Teacher import Teacher
from Person import Person

class School:

    def __init__(self, name, address):
        """initialize the attributes"""
        self._name = name
        self._address = address
        self._people = []

    def add_person(self, person):
        """add person to _people array"""
        self._people.append(person)

    def del_person(self, id):
        """delete person in _people array"""
        for person in self._people:
            if person._id == id:
                self._people.remove(person)

    def get_all_by_firstname(self, fname):
        """get all people with specific firstname"""
        people_list = []
        for person in self._people:
            if person._fname == fname:
                people_list.append(person)
        return people_list


if __name__ == "__main__":
    school1 = School('BCIT', '7671 17th ave')
    staff1 = Staff(1,'Paul','Chen',22, 20000,'instructor')
    school1.add_person(staff1)
    school1.del_person(1)
    student1 = Student(3, 'Bob', 'Bob', 999, 99999, 'ACIT 2515')
    student2 = Student(4, 'Bob', 'Bob', 999, 99999, 'ACIT 2515')
    student3 = Student(5, 'Bob', 'Bob', 999, 99999, 'ACIT 2515')

    school1.add_person(student1)
    school1.add_person(student2)
    school1.add_person(student3)
    school1.del_person(3)

    school1.get_all_by_firstname('Bob')
    school1.get_all_by_firstname('Bob')
    for person in school1.get_all_by_firstname('Bob'):
        person.get_details()