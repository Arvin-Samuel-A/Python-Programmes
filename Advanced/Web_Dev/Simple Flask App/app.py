import os

from flask import Flask
from flask import render_template
from flask import request

import matplotlib.pyplot as plt

def Student_Id_Data(Student_Id):

    Student_Id=int(Student_Id)

    File=open("Advanced/Web_Dev/Simple Flask App/data.csv", "r")
    File.readline()
    
    Data=[]

    for x in File.readlines():

        Var=x.split(", ")
        Var=list(map(int, Var))

        Data.append(Var)

    Result=[]
    Sum=0

    for x in Data:

        if (x[0]==Student_Id):

            Result.append(x)
            Sum+=x[2]

    File.close()

    if Result==[]:
        
        raise Exception("Wrong Inputs")
    
    return (Result, Sum)


def Course_Id_Data(Course_Id):

    Course_Id=int(Course_Id)

    File=open("Advanced/Web_Dev/Simple Flask App/data.csv", "r")
    File.readline()

    Data=[]

    for x in File.readlines():

        Var=x.split(", ")
        Var=list(map(int, Var))

        Data.append(Var)

    Sum=Counter=Max=0
    Marks=[]

    for x in Data:

        if (x[1]==Course_Id):

            if (x[2]>Max):

                Max=x[2]

            Sum+=x[2]
            Counter+=1

            Marks.append(x[2])

    File.close()

    if Marks==[]:

        raise Exception("Wrong Inputs")

    Marks=list(map(int, Marks))

    try:

        plt.clf()

    except:

        pass

    plt.hist(Marks)
    plt.xlabel("Marks")
    plt.ylabel("Frequency")

    plt.savefig("Advanced/Web_Dev/Simple Flask App/static/histogram.jpg")

    return (format(Sum/Counter, ".1f"), Max)


app=Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def Home():

    if request.method=="GET":

        return render_template("index.html")

    elif request.method=="POST":

        try:

            if request.form["ID"]=="student_id":

                Value=request.form["id_value"]
                Data, Total = Student_Id_Data(Value)

                return render_template("student.html", data=Data, total_marks_data=Total)

            elif request.form["ID"]=="course_id":

                Value=request.form["id_value"]
                Avg, Max = Course_Id_Data(Value)
                                        
                return render_template("course.html", average_marks=Avg, maximum_marks=Max)
        
            else:

                return render_template("error.html")
            
        except:

            return render_template("error.html")
        
if __name__=="__main__":

    app.run()