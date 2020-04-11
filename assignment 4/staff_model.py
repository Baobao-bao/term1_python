from peewee import SqliteDatabase, Model, CharField, IntegerField, BooleanField
from person_model import Person
import json
import requests
db = SqliteDatabase("schools.sqlite")
db.connect()

class Staff_m(Person):
    salary = IntegerField()
    position = CharField()

    class Meta: 
        database = db 

    def get_salary(self):
        """return salary"""
        return self._salary

    def get_position(self):
        """return position"""
        return self._position

    def to_dict(self):
        result = dict()
        result["fname"] = self.fname
        result["lname"] = self.lname
        result["id"] = self.id
        result["age"] = self.age
        result["salary"] = self.salary
        result["position"] = self.position
        return result

    def post(self):
        info = self.to_dict()
        into_sql = Staff_m.create(id=info["id"], fname=info["fname"], lname=info["lname"], age=info["age"], position=info["position"], salary=info["salary"])
