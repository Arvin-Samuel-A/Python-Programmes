from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, fields, marshal_with

import os
from flask_cors import CORS
current_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
CORS(app)
Var=os.path.join(current_dir, "api_database.sqlite3")

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
    student_id = db.Column(db.Integer, db.ForeignKey("student.student_id"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("course.course_id"), nullable=False)




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

Enrollment_Output = {

    "enrollment_id" : fields.Integer,
    "student_id" : fields.Integer,
    "course_id" : fields.Integer

}


class API_Course(Resource):

    def get(self, course_id):

        course = Course.query.filter_by(course_id=course_id).first()

        if (course is None):

            response = make_response("", 404)

            return response
        
        return self.Format(course)
    
    def put(self, course_id):

        course = Course.query.filter_by(course_id=course_id).first()

        if (course is None):

            response = make_response("", 404)

            return response
        
        try:

            course_name = request.json["course_name"]

            if (course_name is None):

                response = make_response({"error_code": "COURSE001", "error_message": "Course Name is required"}, 400)

                return response

        except:

            response = make_response({"error_code": "COURSE001", "error_message": "Course Name is required"}, 400)

            return response

        try:

            course_code = request.json["course_code"]

            if (course_code is None):

                response = make_response({"error_code": "COURSE002", "error_message": "Course Code is required"}, 400)

                return response

        except:

            response = make_response({"error_code": "COURSE002", "error_message": "Course Code is required"}, 400)

            return response
        
        try:
                    
            course_description = request.json["course_description"]

        except:

            pass
        
        course.course_name = course_name
        course.course_code = course_code
        course.course_description = course_description

        db.session.commit()

        return self.Format(course)
    
    def delete(self, course_id):

        course = Course.query.filter_by(course_id=course_id).first()

        if (course is None):

            response = make_response("", 404)

            return response
        
        db.session.delete(course)
        db.session.commit()

        response = make_response("", 200)

        return response
    
    def post(self):

        try:

            course_name = request.json["course_name"]

            if (course_name is None):

                response = make_response({"error_code": "COURSE001", "error_message": "Course Name is required"}, 400)

                return response

        except:

            response = make_response({"error_code": "COURSE001", "error_message": "Course Name is required"}, 400)

            return response

        try:

            course_code = request.json["course_code"]

            if (course_code is None):

                response = make_response({"error_code": "COURSE002", "error_message": "Course Code is required"}, 400)

                return response

        except:

            response = make_response({"error_code": "COURSE002", "error_message": "Course Code is required"}, 400)

            return response
        
        try:
                    
            course_description = request.json["course_description"]

        except:

            pass

        course = Course.query.filter_by(course_code=course_code).first()
        
        if course is not None:

            response = make_response("", 409)

            return response
        
        course = Course(course_name=course_name, course_code=course_code, course_description=course_description)

        db.session.add(course)
        db.session.commit()

        return self.Format(course), 201

    @marshal_with(Course_Output)
    def Format(self, Obj):

        return Obj

class API_Student(Resource):

    def get(self, student_id):

        student = Student.query.filter_by(student_id=student_id).first()

        if (student is None):

            response = make_response("", 404)

            return response
        
        return self.Format(student)
    
    def put(self, student_id):

        student = Student.query.filter_by(student_id=student_id).first()

        if (student is None):

            response = make_response("", 404)

            return response
        
        try:

            roll_number = request.json["roll_number"]

            if (roll_number is None):

                response = make_response({"error_code": "STUDENT001", "error_message": "Roll Number required"}, 400)

                return response

        except:

            response = make_response({"error_code": "STUDENT001", "error_message": "Roll Number required"}, 400)

            return response
        
        try:

            first_name = request.json["first_name"]

            if (first_name is None):

                response = make_response({"error_code": "STUDENT002", "error_message": "First Name is required"}, 400)

                return response

        except:

            response = make_response({"error_code": "STUDENT002", "error_message": "First Name is required"}, 400)

            return response

        try:

            last_name = request.json["last_name"]

        except:

            pass

        if (roll_number is None):
            
            response = make_response({"error_code": "STUDENT001", "error_message": "Roll Number required"}, 400)

            return response
        
        if (first_name is None):
            
            response = make_response({"error_code": "STUDENT002", "error_message": "First Name is required"}, 400)

            return response
        
        student.roll_number = roll_number
        student.first_name = first_name
        student.last_name = last_name

        db.session.commit()

        return self.Format(student)
    
    def delete(self, student_id):

        student = Student.query.filter_by(student_id=student_id).first()
        enrollments = Enrollments.query.filter_by(student_id=student_id)

        if (student is None):

            response = make_response("", 404)

            return response
        
        if (enrollments.first() is not None):
        
            for enrollment in enrollments:

                db.session.delete(enrollment)
            
            db.session.flush()


        db.session.delete(student)
        db.session.commit()

        response = make_response("", 200)

        return response
    
    def post(self):

        try:

            roll_number = request.json["roll_number"]

            if (roll_number is None):

                response = make_response({"error_code": "STUDENT001", "error_message": "Roll Number required"}, 400)

                return response

        except:

            response = make_response({"error_code": "STUDENT001", "error_message": "Roll Number required"}, 400)

            return response
        
        try:

            first_name = request.json["first_name"]

            if (first_name is None):

                response = make_response({"error_code": "STUDENT002", "error_message": "First Name is required"}, 400)

                return response

        except:

            response = make_response({"error_code": "STUDENT002", "error_message": "First Name is required"}, 400)

            return response

        try:

            last_name = request.json["last_name"]

        except:

            pass

        student = Student.query.filter_by(roll_number=roll_number).first()
        
        if student is not None:

            response = make_response("", 409)

            return response
        
        student = Student(roll_number=roll_number, first_name=first_name, last_name=last_name)

        db.session.add(student)
        db.session.commit()

        return self.Format(student), 201

    @marshal_with(Student_Output)
    def Format(self, Obj):

        return Obj

class API_Enrollments(Resource):

    def get(self, student_id):

        student = Student.query.filter_by(student_id=student_id).first()

        if (student is None):

            response = make_response({"error_code": "ENROLLMENT002", "error_message": "Student does not exist"}, 400)

            return response

        enrollments = Enrollments.query.filter_by(student_id=student_id)

        if (enrollments.first() is None):

            response = make_response("", 404)

            return response

        Response = []
        
        for x in enrollments:

            Response.append(self.Format(x))

        return Response, 200
    
    def post(self, student_id):

        student = Student.query.filter_by(student_id=student_id).first()

        if (student is None):

            response = make_response("", 404)

            return response
        
        course_id = request.json["course_id"]

        course = Course.query.filter_by(course_id=course_id).first()

        if (course is None):

            response = make_response({"error_code": "ENROLLMENT001", "error_message": "Course does not exist"}, 400)

            return response

        enrollments = Enrollments.query.filter_by(student_id=student_id)
        new_enrollment = Enrollments(student_id=student_id, course_id=course_id)

        db.session.add(new_enrollment)
        db.session.commit()

        Response = []
        
        for x in enrollments:

            Response.append(self.Format(x))

        return Response, 201

    def delete(self, student_id, course_id):

        student = Student.query.filter_by(student_id=student_id).first()

        if (student is None):

            response = make_response({"error_code": "ENROLLMENT002", "error_message": "Student does not exist"}, 400)

            return response
        
        course = Course.query.filter_by(course_id=course_id).first()

        if (course is None):

            response = make_response({"error_code": "ENROLLMENT001", "error_message": "Course does not exist"}, 400)

            return response

        enrollments = Enrollments.query.filter(Enrollments.student_id==student_id and Enrollments.course_id==course_id)

        if (enrollments.first() is None):

            response = make_response("", 404)

            return response

        for enrollment in enrollments:

            db.session.delete(enrollment)

        db.session.commit()

        response = make_response("", 200)

        return response
        

    @marshal_with(Enrollment_Output)
    def Format(self, Obj):

        return Obj



api.add_resource(API_Course, "/api/course/<int:course_id>", "/api/course")
api.add_resource(API_Student, "/api/student/<int:student_id>", "/api/student")
api.add_resource(API_Enrollments, "/api/student/<int:student_id>/course", "/api/student/<int:student_id>/course/<int:course_id>")

if __name__ == "__main__":

    app.run()