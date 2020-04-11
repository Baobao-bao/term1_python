from Person import Person


class Student(Person):

    @staticmethod
    def check_value(num,min=-1000,max=1000,message=''):
        """check if the number is in the correct range"""
        if not (min< num < max):
            print(message)
            raise TypeError

    @staticmethod
    def check_type(val,t1,t2=0):
        """check if the type of arguemnt is correct"""
        if type(val) != t1 and type(val) != t2:
            raise TypeError




    def __init__(self, id, fname, lname, age, tuition, courses):
        """initialize the attributes"""

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
        result["courses"] = self._courses
        result["tuition"] = self._tuition
        result["fname"] = self._fname
        result["lname"] = self._lname
        result["id"] = self.id
        result["age"] = self._age
        return result
