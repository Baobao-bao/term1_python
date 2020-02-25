from Person import Person

class Student(Person):
    def __init__(self, id, fname, lname, age, tuition, courses):
        """initialize the attributes"""
        super(Student, self). __init__(id, fname, lname, age)
        self._tuition = tuition
        self._courses = courses

    def get_tuition(self):
        """return tuition"""
        return self._tuition

    def get_courses(self):
        """return courses"""
        return self._courses