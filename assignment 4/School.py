from Staff import Staff
from Student import Student
from Teacher import Teacher
from Person import Person


class School():

    @staticmethod
    def check_value(num,min=-100000000000000000,max=100000000000000000,massage=''):
        """check if the number is in the correct range"""
        if not (min< num < max):
            print(massage)
            raise TypeError

    @staticmethod
    def check_type(val,t1,t2=0):
        """check if the type of arguemnt is correct"""
        if type(val) != t1 and type(val) != t2:
            raise TypeError

    def __init__(self, name, address):
        """initialize the attributes"""

        School.check_type(name,str)
        School.check_type(address,str)

        self._name = name
        self._address = address
        self._people = []
    
    def get_by_id(self, id):
        for person in self._people:
            if person.id == id:
                return person

    def get_all(self):
        for person in self._people:
            return person

    def add_person(self, person):
        """add person to _people array"""
        self._people.append(person)

    def del_person(self, id):
        """delete person in _people array"""
        for person in self._people:
            if person.id == id:
                self._people.remove(person)

    def get_all_by_firstname(self, fname):
        """get all people with specific firstname"""
        people_list = []
        for person in self._people:
            if person._fname == fname:
                people_list.append(person)
        return people_list

    def to_dict(self):
        output = []
        for person in self._people:
            json = [person.to_dict()]
            output.append(json)
        return output

    def get_stats(self):
        student_counter = 0
        staff_counter = 0
        teacher_counter = 0
        for person in self._people:
            if person.type == "staff":
                staff_counter += 1
            if person.type == "student":
                student_counter += 1
            if person.type == "teacher":
                teacher_counter += 1
        msg = f"There is {student_counter} students, {staff_counter} staff and {teacher_counter} teachers in {self._name}"
        return msg
        
    def update_person(self, id, person):
        self.del_person(id)
        self.add_person(person)





    def _read_from_file(self):
        pass

    def _write_to_file(self):
        pass


if __name__ == "__main__":
    school1 = School('BCIT', '7671 17th ave')
    staff1 = Staff(1,'Paul','Chen',22, 20000,'instructor')
    school1.add_person(staff1)
    school1.del_person(1)
    student1 = Student(3, 'Bob', 'Bob', 21, 99999, 'ACIT 2515')
    student2 = Student(4, 'Bob', 'Bob', 22, 99999, 'ACIT 2515')
    student3 = Student(5, 'Bob', 'Bob', 23, 99999, 'ACIT 2515')

    school1.add_person(student1)
    school1.add_person(student2)
    school1.add_person(student3)
    school1.del_person(3)

    school1.get_all_by_firstname('Bob')
    school1.get_all_by_firstname('Bob')
    for person in school1.get_all_by_firstname('Bob'):
        person.get_details()