from flask import Flask, jsonify
app = FLask(__name__)

@app.route('/advance_students/')
def advance_students():
    result = [student for student in students if student['age'] < 21 and student['grade'] == 'A']
    return jsonify(result)

@app.route('/student_names/')
def student_names():
    result = [{"first_name": student['first_name'], "last_name": student['last_name']} for student in students]
    return jsonify(result)

@app.route('/student_ages/')
def student_ages():
    result = [{"student_name": f"{student['first_name']} {student['last_name']}", "age": student['age']} for student in students]
    return jsonify(result)

@app.route('/students/')
def all_students():
    return jsonify(students)