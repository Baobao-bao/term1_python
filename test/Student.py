from Person import Person

class Student(Person):

    @staticmethod
    def check_value(num,min=-100000000000000000,max=100000000000000000,massage=''):
        """check if the number is in the correct range"""
        if not (min< num < max):
            print(massage)
            raise ValueError

    @staticmethod
    def check_type(val,t1,t2=0):
        """check if the type of arguemnt is correct"""
        if type(val) != t1 and type(val) != t2:
            raise TypeError




    def __init__(self, id, fname, lname, age, tuition, courses):
        """initialize the attributes"""


        Student.check_type(id,int)
        Student.check_value(id,0)

        Student.check_type(fname,str)
        Student.check_type(lname,str)

        Student.check_type(age,int)
        Student.check_value(age,0,120)

        Student.check_type(tuition,int)
        Student.check_value(tuition,0,1000000000)

        Student.check_type(courses,str)

        super(Student, self). __init__(id, fname, lname, age)
        self._tuition = tuition
        self._courses = courses
        self.type = "student"

    def get_tuition(self):
        """return tuition"""
        return self._tuition

    def get_courses(self):
        """return courses"""
        return self._courses

    def to_dict(self):
        result = dict()
        result["fname"] = self._fname
        result["lname"] = self._lname
        result["id"] = self._id
        result["age"] = self._age
        result["tuition"] = self._tuition
        result["courses"] = self._courses
        return result