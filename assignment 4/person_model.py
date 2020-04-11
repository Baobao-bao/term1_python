from peewee import SqliteDatabase, Model, CharField, IntegerField, BooleanField, ForeignKeyField
# from school_model import School

# tea = Teacher(id=33, fname="Paul", lname="Chen", age="22", _salary=2, _courses="ACIT 2515")

db = SqliteDatabase("schools.sqlite")
db.connect()

class Person(Model):
    """ Abstract Class Person """
    id = IntegerField(unique=True)
    fname = CharField()
    lname = CharField()
    age = IntegerField()

    class Meta:
        database = db

    def getid(self):
        """return id"""
        return self.id

    def get_fname(self):
        """return first name"""
        return self.fname

    def getlname(self):
        """return last name"""
        return self.lname

    def get_age(self):
        """return age"""
        return self.age

    def get_details(self):
        """return details"""
        print('ID number', str(self.id)+',', self.fname, self.lname, self.age)
    
    def to_dict(self):
        result = dict()
        result["fname"] = self.fname
        result["lname"] = self.lname
        result["id"] = self.id
        result["age"] = self.age
        return result