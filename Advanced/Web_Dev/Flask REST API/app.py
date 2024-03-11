from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, fields, marshal_with
from werkzeug.exceptions import HTTPException

import os
from flask_cors import CORS
current_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
CORS(app)
Var=os.path.join(current_dir, "api_database.sqlite3")
print(Var)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+Var

db = SQLAlchemy()

api = Api(app)
db.init_app(app)

app.app_context().push()




class Course(db.Model):

    __tablename__ = "course"

    course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_code = db.Column(db.String, unique=True, nullable=False)
    course_name = db.Column(db.String, nullable=False)
    course_description = db.Column(db.String)


class Student(db.Model):

    __tablename__ = "student"

    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    roll_number = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String)

    courses = db.relationship("Course", secondary="enrollments")


class Enrollments(db.Model):

    __tablename__ = "enrollments"

    enrollment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.student_id", ondelete="CASCADE"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("course.course_id", ondelete="CASCADE"), nullable=False)



class NotFoundError(HTTPException):

    def __init__(self, status_code):

        self.response = make_response("", status_code)


class InputError(HTTPException):

    def __init__(self, status_code, error_code, error_message):

        self.response = make_response({"error_code": error_code, "error_message": error_message}, status_code)


Course_Output = {

    "course_id" : fields.Integer,
    "course_name" : fields.String,
    "course_code" : fields.String,
    "course_description" : fields.String

}

Student_Output = {

    "student_id" : fields.Integer,
    "first_name" : fields.String,
    "last_name" : fields.String,
    "roll_number" : fields.String

}


class API_Course(Resource):

    @marshal_with(Course_Output)
    def get(self, course_id):

        course = Course.query.filter_by(course_id=course_id).first()

        if (course is None):

            raise NotFoundError(404)
        
        return course
    
    @marshal_with(Course_Output)
    def put(self, course_id):

        course = Course.query.filter_by(course_id=course_id).first()

        if (course is None):

            raise NotFoundError(404)
        
        course_name = request.json["course_name"]
        course_code = request.json["course_code"]
        course_description = request.json["course_description"]

        if (course_name is None):

            raise InputError(400, "COURSE001", "Course Name is required")
        
        if (course_code is None):

            raise InputError(400, "COURSE002", "Course Code is required")
        
        course.course_name = course_name
        course.course_code = course_code
        course.course_description = course_description

        db.session.commit()

        return course
    
    def delete(self, course_id):

        course = Course.query.filter_by(course_id=course_id).first()

        if (course is None):

            raise NotFoundError(404)
        
        db.session.delete(course)
        db.session.commit()

        response = make_response("", 200)

        return response
    
    @marshal_with(Course_Output)
    def post(self):

        course_name = request.json["course_name"]
        course_code = request.json["course_code"]
        course_description = request.json["course_description"]

        course = Course.query.filter_by(course_code=course_code).first()
        
        if (course_name is None):

            raise InputError(400, "COURSE001", "Course Name is required")
        
        if (course_code is None):

            raise InputError(400, "COURSE002", "Course Code is required")
        
        if course is not None:

            raise NotFoundError(409)
        
        course = Course(course_name=course_name, course_code=course_code, course_description=course_description)

        db.session.add(course)
        db.session.commit()

        return course, 201



        
        



api.add_resource(API_Course, "/api/course/<int:course_id>", "/api/course")
#api.add_resource(API_Student, "/api/student/<int:student_id>", "/api/student")
#api.add_resource(API_Enrollments, "/api/student/<int:student_id>/course", "/api/student/<int:student_id>/course/<int:course_id")

if __name__ == "__main__":

    app.run()