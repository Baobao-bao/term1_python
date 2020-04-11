from peewee import SqliteDatabase, Model, CharField, IntegerField, BooleanField
from person_model import Person
import requests
import json

db = SqliteDatabase("schools.sqlite")
db.connect()

class Student_m(Person):
    tuition = IntegerField()
    courses = CharField()

    class Meta:
        database = db

    def get_tuition(self):
        """return tuition"""
        return self.tuition

    def get_courses(self):
        """return courses"""
        return self.courses

    def to_dict(self):
        result = dict()
        result["courses"] = self.courses
        result["tuition"] = self.tuition
        result["fname"] = self.fname
        result["lname"] = self.lname
        result["id"] = self.id
        result["age"] = self.age
        return result
    
    def post(self):
        info = self.to_dict()
        into_sql = Student_m.create(id=info["id"], fname=info["fname"], lname=info["lname"], age=info["age"], courses=info["courses"], tuition=info["tuition"])
        js = json.dumps(self.to_dict())

    def get_by_id(self,id):
        query = Student_m.select().where(Student_m.id == id)
        print(query)
        return query

if __name__ == "__main__":
    pass



