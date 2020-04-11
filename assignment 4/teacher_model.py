from peewee import SqliteDatabase, Model, CharField, IntegerField, BooleanField
import sqlite3
from person_model import Person
import json
import requests

db = SqliteDatabase("schools.sqlite")
db.connect()

class Teacher_m(Person):
    salary = IntegerField()
    courses = CharField()

    class Meta: 
        database = db

    def get_salary(self):
        """return salary"""
        return self.salary

    def get_courses(self):
        """return courses"""
        return self.courses

    def to_dict(self):
        result = dict()
        result["id"] = self.id
        result["fname"] = self.fname
        result["lname"] = self.lname
        result["age"] = self.age
        result["salary"] = self.salary
        result["courses"] = self.courses
        return result

    def post(self):
        info = self.to_dict()
        into_sql = Teacher_m.create(id=info["id"], fname=info["fname"], lname=info["lname"], age=info["age"], courses=info["courses"], salary=info["salary"])

