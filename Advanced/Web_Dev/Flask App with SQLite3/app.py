import os

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

current_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(current_dir, "database.sqlite3")

db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

class Student(db.Model):

    __tablename__ = "student"

    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    roll_number = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String)

    courses = db.relationship("Course", secondary="enrollments")

class Course(db.Model):

    __tablename__ = "course"

    course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_code = db.Column(db.String, unique=True, nullable=False)
    course_name = db.Column(db.String, nullable=False)
    course_description = db.Column(db.String)

class Enrollments(db.Model):

    __tablename__ = "enrollments"

    enrollment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    estudent_id = db.Column(db.Integer, db.ForeignKey("student.student_id"), nullable=False)
    ecourse_id = db.Column(db.Integer, db.ForeignKey("course.course_id"), nullable=False)


@app.route("/")
def index():

    students=Student.query.all()
    count=Student.query.count()
        
    return render_template("index.html", Students=students, Count=count)


@app.route("/student/create", methods=["GET", "POST"])
def Create():
        
    if request.method == "GET":

        return render_template("create.html")
    

    elif request.method == "POST":

        roll_number = request.form.get("roll")

        if (Student.query.filter_by(roll_number=roll_number).count()):

            return render_template("error.html")
        
        first_name = request.form.get("f_name")
        last_name = request.form.get("l_name")

        student = Student(roll_number=roll_number, first_name=first_name, last_name=last_name)

        courses=request.form.getlist("courses")

        if "course_1" in courses:

            course_1 = Course.query.filter_by(course_code="CSE01").first()
            student.courses.append(course_1)

        if "course_2" in courses:

            course_2 = Course.query.filter_by(course_code="CSE02").first()
            student.courses.append(course_2)

        if "course_3" in courses:

            course_3 = Course.query.filter_by(course_code="CSE03").first()
            student.courses.append(course_3)

        if "course_4" in courses:

            course_4 = Course.query.filter_by(course_code="BST13").first()
            student.courses.append(course_4)

        db.session.add(student)
        db.session.commit()

        return redirect("/")
    

@app.route("/student/<int:student_id>/update", methods=["GET", "POST"])
def Update(student_id):

    student = Student.query.filter_by(student_id=student_id).first()

    if request.method == "GET":

        return render_template("update.html", Student=student)

    elif request.method == "POST":

        student.first_name = request.form.get("f_name")
        student.last_name = request.form.get("l_name")

        courses=request.form.getlist("courses")

        enrollments = Enrollments.query.filter_by(estudent_id=student_id)

        for x in enrollments:

            db.session.delete(x)

        if "course_1" in courses:

            course_1 = Course.query.filter_by(course_code="CSE01").first()
            student.courses.append(course_1)

        if "course_2" in courses:

            course_2 = Course.query.filter_by(course_code="CSE02").first()
            student.courses.append(course_2)

        if "course_3" in courses:

            course_3 = Course.query.filter_by(course_code="CSE03").first()
            student.courses.append(course_3)

        if "course_4" in courses:

            course_4 = Course.query.filter_by(course_code="BST13").first()
            student.courses.append(course_4)

        db.session.add(student)
        db.session.commit()

        return redirect("/")
    
    
@app.route("/student/<int:student_id>/delete")
def Delete(student_id):

    student = Student.query.filter_by(student_id=student_id).first()

    db.session.delete(student)
    db.session.commit()

    return redirect("/")


@app.route("/student/<int:student_id>", methods=["GET", "POST"])
def View(student_id):

    student = Student.query.filter_by(student_id=student_id).first()

    return render_template("personal.html", Student=student, Courses=student.courses)


if __name__ == "__main__":

    app.run(debug=True, host="0.0.0.0")