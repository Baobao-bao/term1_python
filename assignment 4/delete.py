from peewee import SqliteDatabase, Model, CharField, IntegerField, ForeignKeyField
# from Person import Person
from School import School
from Teacher import Teacher
from Staff import Staff
from Student import Student


db = SqliteDatabase("schools.sqlite")
db.connect()

# class School(Model):
#     name = CharField(unique=True)
#     class Meta:
#         database = db

# class Person(Model):
#     name = CharField(unique=True)
#     school = ForeignKeyField(School)
#     class Meta:
#         database = db   

if __name__ == "__main__":
    db.drop_tables([School,Teacher,Staff,Student])
    db.create_tables([School, Teacher,Staff,Student])
