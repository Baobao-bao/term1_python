from peewee import *
from person_model import Person
from student_model import Student_m
from staff_model import Staff_m
from teacher_model import Teacher_m
import json
import requests

db = SqliteDatabase("schools.sqlite")
db.connect()

class School(Model):

    address = CharField(unique=True)
    name = CharField()
    class Meta:
        database = db

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


if __name__ == "__main__":
    db.drop_tables([School, Staff ,Teacher, Student_m])


