from flask import Flask, jsonify
import csv

app = Flask(__name__)

def load_students():
    students = []
    with open('students.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
    return students

students = load_students()

@app.route('/advance_students/')
def advance_students():
    result = [student for student in students if student['age'] < 21 and student['grade'] == 'A']
    return jsonify(result)

@app.route('/old_students/')
def old_students():
    result = [student for student in students if student['age'] > 20]
    return jsonify(result)

@app.route('/young_students/')
def young_students():
    result = [student for student in students if student['age'] < 21 ]
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