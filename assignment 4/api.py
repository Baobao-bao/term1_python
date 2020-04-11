from flask import Flask, jsonify, request, make_response
from Staff import Staff
from School import School
from Teacher import Teacher
from Student import Student
from student_model import Student_m
from staff_model import Staff_m
from teacher_model import Teacher_m
import json

app = Flask(__name__)

school = School("BCIT", "111 Kingsway")

@app.route("/school", methods=["GET"])
def list_students():
    try:
        return make_response(jsonify(school.to_dict()), 200)
    except UnboundLocalError:
        return("No entities stored", 400)

@app.route("/school/student", methods=["POST"])
def add_student():
    data = request.json
    if not data:
        return make_response("No JSON. Check headers and JSON format.", 400)
    try:
        student = Student(id=data["id"], fname=data["fname"],lname=data["lname"],age=data["age"], tuition=data["tuition"], courses=data["courses"])
        school.add_person(student)
        Student_model = Student_m(id=data["id"], fname=data["fname"],lname=data["lname"],age=data["age"], tuition=data["tuition"], courses=data["courses"])
        Student_model.post()
        return make_response(str(data["id"]), 200)
    except ValueError as e:
        message = str(e)
        return make_response(message, 400)

@app.route("/school/teacher", methods=["POST"])
def add_teacher():
    data = request.json
    if not data:
        return make_response("No JSON. Check headers and JSON format.", 400)
    try:
        teacher = Teacher(id=data["id"], fname=data["fname"],lname=data["lname"],age=data["age"], salary=data["salary"], courses=data["courses"])
        school.add_person(teacher)
        teacher_model = Teacher_m(id=data["id"], fname=data["fname"],lname=data["lname"],age=data["age"], salary=data["salary"], courses=data["courses"])
        teacher_model.post()
        return make_response(str(data["id"]), 200)
    except ValueError as e:
        message = str(e)
        return make_response(message, 400)

@app.route("/school/staff", methods=["POST"])
def add_staff():
    data = request.json
    if not data:
        return make_response("No JSON. Check headers and JSON format.", 400)
    try:
        staff = Staff(id=data["id"], fname=data["fname"],lname=data["lname"],age=data["age"], salary=data["salary"], position=data["position"])
        school.add_person(staff)
        staff_model = Staff_m(id=data["id"], fname=data["fname"],lname=data["lname"],age=data["age"], salary=data["salary"], position=data["position"])
        staff_model.post()
        return make_response(str(data["id"]), 200)
    except ValueError as e:
        message = str(e)
        return make_response(message, 400)

@app.route("/school/student/<int:student_id>", methods=["GET"])
def get_student(student_id):
    try:
        return jsonify(school.get_by_id(student_id).to_dict())
    except AttributeError as e:
        message = str(e)
        return make_response(message, 400)
    except TypeError as e:
        message = str(e)
        return make_response(message, 400)

@app.route("/school/student/<int:student_id>/delete", methods=["DELETE"])
def delete_student(student_id):
    try:
        school.del_person(student_id)
        student = Student_m.get(Student_m.id == student_id)
        student.delete().execute()
        return make_response("Entity deleted", 200)
    except AttributeError as e:
        message = str(e)
        return make_response(message, 400)

@app.route("/school/teacher/<int:teacher_id>/delete", methods=["DELETE"])
def delete_teacher(teacher_id):
    try:
        school.del_person(teacher_id)
        teacher = Teacher_m.get(Teacher_m.id == teacher_id)
        teacher.delete().execute()
        return make_response("Entity deleted", 200)
    except AttributeError as e:
        message = str(e)
        return make_response(message, 400)

@app.route("/school/staff/<int:staff_id>/delete", methods=["DELETE"])
def delete_staff(staff_id):
    try:
        school.del_person(staff_id)
        staff = Staff_m.get(Staff_m.id == staff_id)
        staff.delete().execute()
        return make_response("Entity deleted", 200)
    except AttributeError as e:
        message = str(e)
        return make_response(message, 400)

@app.route("/school/all/<string:type>", methods=["GET"])
def get_by_type(type):
    list = ["staff","student","teacher"]
    try:
        if type not in list:
            raise TypeError
        for person in school._people:
            if person.type == type:
                return jsonify(person.to_dict())
    except AttributeError as e:
        message = str(e)
        return make_response(message, 400)
    except TypeError as e:
        message = str(e)
        return make_response("Incorrect Type", 400)

@app.route("/school/stats", methods=["GET"])
def get_stats():
    try:
        msg = school.get_stats()
        jsonify(msg)
        print(msg)
        return msg
    except ValueError:
        make_response("Error", 400)

@app.route("/school/update_student/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.json
    if not data:
        return make_response("No JSON. Check headers and JSON format.", 400)
    try:
        student = Student(student_id, data["fname"],data["lname"],data["age"], data["tuition"], data["courses"])
        school.update_person(student_id,student)
        stu = Student_m.get(Student_m.id == student_id)
        stu.delete().execute()
        stu = Student_m.create(id=data["id"], fname=data["fname"], lname=data["lname"],age=data["age"], tuition=data["tuition"],courses= data["courses"])
        stu.save()
        return make_response(str(data["id"]), 200)
    except ValueError as e:
        message = str(e)
        return make_response(message, 400)

@app.route("/school/update_teacher/<int:teacher_id>", methods=["PUT"])
def update_teacher(teacher_id):
    data = request.json
    if not data:
        return make_response("No JSON. Check headers and JSON format.", 400)
    try:
        teacher = Teacher(teacher_id, data["fname"],data["lname"],data["age"], data["salary"], data["courses"])
        school.update_person(teacher_id,teacher)
        tea = Teacher_m.get(Teacher_m.id == teacher_id)
        tea.delete().execute()
        tea = Teacher_m.create(id=data["id"], fname=data["fname"], lname=data["lname"],age=data["age"], salary=data["salary"],courses= data["courses"])
        tea.save()
        return make_response(str(data["id"]), 200)
    except ValueError as e:
        message = str(e)
        return make_response(message, 400)

@app.route("/school/update_staff/<int:staff_id>", methods=["PUT"])
def update_staff(staff_id):
    data = request.json
    if not data:
        return make_response("No JSON. Check headers and JSON format.", 400)
    try:
        staff = Staff(staff_id, data["fname"],data["lname"],data["age"], data["salary"], data["position"])
        school.update_person(staff_id,staff)
        sta = Staff_m.get(Staff_m.id == staff_id)
        sta.delete().execute()
        sta = Staff_m.create(id=data["id"], fname=data["fname"], lname=data["lname"],age=data["age"], position=data["position"],salary= data["salary"])
        sta.save()
        return make_response(str(data["id"]), 200)
    except ValueError as e:
        message = str(e)
        return make_response(message, 400)

if __name__ == "__main__":
    app.run(debug=True)
