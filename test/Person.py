from datetime import *

class Person():
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

    def __init__(self,id, fname, lname, age):
        """initialize the attributes"""
        Person.check_type(id,int)
        Person.check_value(id,0)  

        Person.check_type(fname,str)
        Person.check_type(lname,str)

        Person.check_type(age,int)
        Person.check_value(age,0,120)

        self._id = id
        self._fname = fname
        self._lname = lname
        self._age = age
        self._datestart = date.today()

    def get_id(self):
        """return id"""
        return self._id

    def get_fname(self):
        """return first name"""
        return self._fname

    def get_lname(self):
        """return last name"""
        return self._lname

    def get_age(self):
        """return age"""
        return self._age

    def get_datestart(self):
        """return start date"""
        return self._datestart

    def get_details(self):
        """return details"""
        print('ID number', str(self._id)+',', self._fname, self._lname, self._age, 'years old started on', self._datestart)
    
    def to_dict(self):
        raise NotImplementedError
        # result = dict()
        # result["fname"] = self._fname
        # result["lname"] = self._lname
        # result["_id"] = self._id
        # result["age"] = self._age
        # return result

