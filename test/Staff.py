from Person import Person

class Staff(Person):
    def __init__(self, id, fname, lname, age, salary, position):
        """initialize the attributes"""
        super(Staff, self). __init__(id, fname, lname, age)
        self._salary = salary
        self._position = position

    def get_salary(self):
        """return salary"""
        return self._salary

    def get_position(self):
        """return position"""
        return self._position