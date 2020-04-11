from Person import Person

class Staff(Person):

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

    def __init__(self, id, fname, lname, age, salary, position):
        """initialize the attributes"""

        super(Staff, self). __init__(id, fname, lname, age)
        self._salary = salary
        self._position = position
        self.type = "staff"

    def get_salary(self):
        """return salary"""
        return self._salary

    def get_position(self):
        """return position"""
        return self._position

    def to_dict(self):
        result = dict()
        result["fname"] = self._fname
        result["lname"] = self._lname
        result["id"] = self.id
        result["age"] = self._age
        result["position"] = self._position
        result["salary"] = self._salary
        return result

    