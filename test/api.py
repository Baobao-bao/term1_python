from flask import Flask, jsonify, request, make_response
from Student import Student
from Staff import Staff
from School import School
from Teacher import Teacher



app = Flask(__name__)

school = School("bcit", "111 Kingsway")

@app.route("/school", methods=["GET"])
def list_people():
    try:
        return make_response(jsonify(school.to_dict()), 200)
    except UnboundLocalError:
        return("No entities stored", 400)



@app.route("/school/stats", methods=["GET"])
def get_stats():
    try:
        msg = school.get_stats()
        jsonify(msg)
        print(msg)
        return msg
    except ValueError:
        make_response("Error", 400)

@app.route("/school/student", methods=["POST"])
def add_student():
    data = request.json
    if not data:
        return make_response("No JSON. Check headers and JSON format.", 400)
    try:
        student = Student(data["id"], data["fname"],data["lname"],data["age"], data["tuition"], data["courses"])
        school.add_student(student)
        school.write_to_file()
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
        teacher = Teacher(data["id"], data["fname"],data["lname"],data["age"], data["salary"], data["courses"])
        school.add_teacher(teacher)
        #school.write_to_file()
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
        staff = Staff(data["id"], data["fname"],data["lname"],data["age"], data["salary"], data["position"])
        school.add_staff(staff)
        school.write_to_file()
        return make_response(str(data["id"]), 200)
    except ValueError as e:
        message = str(e)
        return make_response(message, 400)

@app.route("/school/student/<int:student_id>", methods=["GET"])
def get_student(student_id):
    try: 
        return jsonify(school.find_student(student_id).to_dict(), 200)
    except AttributeError as e:
        message = str(e)
        return make_response(message, 400)
    except TypeError as e:
        message = str(e)
        return make_response(message, 400)
    except ValueError as e:
        message = str(e)
        return make_response(message, 404)

@app.route("/school/staff/<int:staff_id>", methods=["GET"])
def get_staff(staff_id):
    try: 
        return jsonify(school.find_staff(staff_id).to_dict(), 200)
    except AttributeError as e:
        message = str(e)
        return make_response(message, 400)
    except TypeError as e:
        message = str(e)
        return make_response(message, 400)
    except ValueError as e:
        message = str(e)
        return make_response(message, 404)

@app.route("/school/teacher/<int:teacher_id>", methods=["GET"])
def get_teacher(teacher_id):
    try: 
        return jsonify(school.find_teacher(teacher_id).to_dict(), 200)
    except AttributeError as e:
        message = str(e)
        return make_response(message, 400)
    except TypeError as e:
        message = str(e)
        return make_response(message, 400)
    except ValueError as e:
        message = str(e)
        return make_response(message, 404)
        
@app.route("/school/student/<int:student_id>/delete", methods=["DELETE"])
def delete_student(student_id):
    try:
        school.remove_student(student_id)
        return make_response("Entity deleted", 200)
    except AttributeError as e:
        message = str(e)
        return make_response(message, 400)
    except ValueError as e:
        message = str(e)
        return make_response(message, 404)

@app.route("/school/staff/<int:staff_id>/delete", methods=["DELETE"])
def delete_staff(staff_id):
    try:
        school.remove_staff(staff_id)
        return make_response("Entity deleted", 200)
    except AttributeError as e:
        message = str(e)
        return make_response(message, 400)
    except ValueError as e:
        message = str(e)
        return make_response(message, 404)

@app.route("/school/teacher/<int:teacher_id>/delete", methods=["DELETE"])
def delete_teacher(teacher_id):
    try:
        school.remove_teacher(teacher_id)
        return make_response("Entity deleted", 200)
    except AttributeError as e:
        message = str(e)
        return make_response(message, 400)
    except ValueError as e:
        message = str(e)
        return make_response(message, 404)
        
if __name__ == "__main__":
    app.run(debug=True)

