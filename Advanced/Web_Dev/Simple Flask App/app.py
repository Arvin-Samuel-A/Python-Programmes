from flask import Flask
import csv

def Student_Id_Data():

    File=open("data.csv", "r")
    File.readline()

    Data=csv.reader(File)

    for x in Data:

        print(x)

#app=Flask(__name__)
Student_Id_Data()