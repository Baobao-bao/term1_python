from Person import Person

class Teacher(Person):
    def __init__(self, id, fname, lname, age, salary, courses):
        """initialize the attributes"""
        super(Teacher, self). __init__(id, fname, lname, age)
        self._salary = salary
        self._courses = courses

    def get_salary(self):
        """return salary"""
        return self._salary

    def get_courses(self):
        """return courses"""
        return self._courses