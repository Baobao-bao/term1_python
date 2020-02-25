from datetime import *

class Person():

    def __init__(self,id, fname, lname, age):
        """initialize the attributes"""
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
