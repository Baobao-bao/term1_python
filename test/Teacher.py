from Person import Person

class Teacher(Person):


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

    
    def __init__(self, id, fname, lname, age, salary, courses):
        """initialize the attributes"""

        Teacher.check_type(id,int)
        Teacher.check_value(id,0)

        Teacher.check_type(fname,str)
        Teacher.check_type(lname,str)

        Teacher.check_type(age,int)
        Teacher.check_value(age,0,120)

        Teacher.check_type(salary,int)
        Teacher.check_value(salary,0,1000000000)

        Teacher.check_type(courses,str)

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
        result["id"] = self._id
        result["age"] = self._age
        result["salary"] = self._salary
        result["courses"] = self._courses
        return result