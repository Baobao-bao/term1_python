from Staff import Staff
from Student import Student
from Teacher import Teacher
from Person import Person
import urllib
import json

from peewee import Model, CharField, IntegerField,DateField  
from database import db 

class School(Model):

    class Meta:
        """database mapping"""
        database = db

    @staticmethod
    def check_value(num,min=-1000,max=1000,massage=''):
        """check if the number is in the correct range"""
        if not (min< num < max):
            print(massage)
            raise ValueError

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

        self._students = dict()
        self._staffs = dict()
        self._teachers = dict()
        self._filepath = "text.txt"

        self._students_li = list()
        self._staffs_li = list()
        self._teachers_li = list()
    
        self._read_from_file()
    
    def _read_from_file(self):
        with open(self._filepath, 'r') as file:
            content = file.read()
            if content:
                json_content = json.loads(content)
                self._name = json_content["name"]
                self._address = json_content["address"]
                self._students_li = json_content["students"]
                for student in self._students_li:
                    student = Student(student["id"],student["fname"],student["lname"],student["age"],student["tuition"],student["courses"])
                self.add_student(student)

                self._staffs_li = json_content["staffs"]
                for staff in self._staffs_li:
                    staff = Staff(staff["id"],staff["fname"],staff["lname"],staff["age"],staff["salary"],staff["position"])
                    self.add_staff(staff)

                self._teachers_li = json_content["teachers"]
                for teacher in self._teachers_li:
                    teacher = Teacher(teacher["id"],teacher["fname"],teacher["lname"],teacher["age"],teacher["salary"],teacher["courses"])
                    self.add_teacher(teacher)
    
    def write_to_file(self):
        with open(self._filepath, 'w') as outfile:
            to_write = json.dumps(self.to_dict())
            outfile.write(to_write)
        
    def get_address(self):
        """ Getter for private address """
        return self._address

    def get_stats(self):
        student_counter = len(self._students)
        staff_counter = len(self._staffs)
        teacher_counter = len(self._teachers)
            
        msg = f"There is {student_counter} students, {staff_counter} staff and {teacher_counter} teachers in {self._name}"
        return msg

    def add_student(self, student):
        """ Add student to dictionary
            raises Exception if wrong type or student already exists
            returns True otherwise """

        if type(student) is not Student:
            raise ValueError("Can only add students")

        if student.get_id() in self._students.keys():
            raise ValueError("Student already in school")

        self._students[student.get_id()] = student
        # self._write_to_file()
        return True




    def find_student(self, student_id):
        """ Get student from dictionary, returns None if no student found """
        if student_id not in self._students.keys():
            raise ValueError("Student not found")
        
        return self._students.get(student_id)

    def remove_student(self, student_id):
        """ Removes a student based on the ID """
        if not self.find_student(student_id):
            raise ValueError("Student not found.")
        else:
            del self._students[student_id]

    def add_staff(self, staff):
        """ Add staff to dictionary
            raises Exception if wrong type or staff already exists
            returns True otherwise """

        if type(staff) is not Staff:
            raise ValueError("Can only add staffs")

        if staff.get_id() in self._staffs.keys():
            raise ValueError("Staff already in school")

        self._staffs[staff.get_id()] = staff
        return True

    def find_staff(self, staff_id):
        """ Get staff from dictionary, returns None if no staff found """
        if staff_id not in self._staffs.keys():
            raise ValueError("staff not found")
        
        return self._staffs.get(staff_id)


    def remove_staff(self, staff_id):
        """ Removes a staff based on the ID """
        if not self.find_staff(staff_id):
            raise ValueError("staff not found.")
        else:
            del self._staffs[staff_id]


    def add_teacher(self, teacher):
        """ Add teacher to dictionary
            raises Exception if wrong type or teacher already exists
            returns True otherwise """

        if type(teacher) is not Teacher:
            raise ValueError("Can only add teachers")

        if teacher.get_id() in self._teachers.keys():
            raise ValueError("Teacher already in school")

        self._teachers[teacher.get_id()] = teacher
        return True


    def find_teacher(self, teacher_id):
        """ Get teacher from dictionary, returns None if no teacher found """
        if teacher_id not in self._teachers.keys():
            raise ValueError("teacher not found")
        
        return self._teachers.get(teacher_id)

    def remove_teacher(self, teacher_id):
        """ Removes a teacher based on the ID """
        if not self.find_teacher(teacher_id):
            raise ValueError("teacher not found.")
        else:
            del self._teachers[teacher_id]



    # def add_person(self, person):
    #     """add person to _people array"""
    #     self._people.append(person)

    # def del_person(self, id):
    #     """delete person in _people array"""
    #     for person in self._people:
    #         if person._id == id:
    #             self._people.remove(person)

    # def get_all_by_firstname(self, fname):
    #     """get all people with specific firstname"""
    #     people_list = []
    #     for person in self._people:
    #         if person._fname == fname:
    #             people_list.append(person) 
    #     return people_list

    def to_dict(self):
        # dict = dict()
        result = dict()
        result["name"] = self._name
        result["address"] = self._address
        result["students"] = list()
        result["staffs"] = list()
        result["teachers"] = list()
        for student in self._students.values():
            result["students"].append(student.to_dict())
        for staff in self._staffs.values():
            result["staffs"].append(staff.to_dict())
        for teacher in self._teachers.values():
            result["teachers"].append(teacher.to_dict())
        return result


# if __name__ == "__main__":
#     school1 = School('BCIT', '7671 17th ave')
#     staff1 = Staff(1,'Paul','Chen',22, 20000,'instructor')
#     school1.add_person(staff1)
#     school1.del_person(1)
#     student1 = Student(3, 'Bob', 'Bob', 21, 99999, 'ACIT 2515')
#     student2 = Student(4, 'Bob', 'Bob', 22, 99999, 'ACIT 2515')
#     student3 = Student(5, 'Bob', 'Bob', 23, 99999, 'ACIT 2515')

#     school1.add_person(student1)
#     school1.add_person(student2)
#     school1.add_person(student3)
#     school1.del_person(3)

#     school1.get_all_by_firstname('Bob')
#     school1.get_all_by_firstname('Bob')
#     for person in school1.get_all_by_firstname('Bob'):
#         person.get_details()
if __name__ == "__main__":
    BCIT = School("BCIT", "111 Kingsway")


    