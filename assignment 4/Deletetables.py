from peewee import *
from person_model import Person
from student_model import Student_m
from staff_model import Staff_m
from teacher_model import Teacher_m


db = SqliteDatabase("schools.sqlite")
db.connect()

if __name__ == "__main__":
    db.drop_tables([Staff_m, Teacher_m, Student_m])