from Person import Person

class Teacher(Person):

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
    
    def __init__(self, id, fname, lname, age, salary, courses):
        """initialize the attributes"""

        super(Teacher, self). __init__(id, fname, lname, age)
        self._salary = salary
        self._courses = courses
        self.type = "teacher"

    def get_salary(self):
        """return salary"""
        return self._salary

    def get_courses(self):
        """return courses"""
        return self._courses
    
    def to_dict(self):
        result = dict()
        result["fname"] = self._fname
        result["lname"] = self._lname
        result["id"] = self.id
        result["age"] = self._age
        result["position"] = self._courses
        result["salary"] = self._salary
        return result