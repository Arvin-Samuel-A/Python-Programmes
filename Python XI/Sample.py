'''for i in range(0,9,2):
    for j in range(1,i,2):
        print(j, end=" ")
    print()

Num=int(input("Enter a Number to create a pattern : "))

for i in range(Num,0,-1):
    for j in range(Num,i-1,-1):
        print(j, end=" ")
    print()

for i in range(1,6):
    for j in range(i):
        print(i, end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

L=[10,20,30,40,50,60,70,80,90,100]
Sum=0

for i in range(0,len(L),2):
    Sum+=L[i]

print(Sum)    

L=[15,16,75,78,75,23,85,95,85]
Sum=0

for i in L:
    if i%5==0 and i%10!=0:
        Sum+=i

print(Sum)

from tkinter import *

root=Tk()
root.geometry('100x100')
btn=Button(root, text='Click Me !', command=root.destroy)
btn.pack(side='top')
root.mainloop()'''

import numpy as np
import matplotlib.pyplot as plt

'''categories = ['Food Quality', 'Food Variety', 'Service Quality', 'Ambiance', 'Affordability']
categories = [*categories, categories[0]]

restaurant_1 = [4, 4, 5, 4, 3]
restaurant_2 = [5, 5, 4, 5, 2]
restaurant_3 = [3, 4, 5, 3, 5]
restaurant_1 = [*restaurant_1, restaurant_1[0]]
restaurant_2 = [*restaurant_2, restaurant_2[0]]
restaurant_3 = [*restaurant_3, restaurant_3[0]]

label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(restaurant_1))

plt.figure(figsize=(8, 8))
plt.subplot(polar=True)
plt.plot(label_loc, restaurant_1, label='Restaurant 1')
plt.plot(label_loc, restaurant_2, label='Restaurant 2')
plt.plot(label_loc, restaurant_3, label='Restaurant 3')
plt.title('Restaurant comparison', size=20, y=1.05)
lines, labels = plt.thetagrids(np.degrees(label_loc), labels=categories)
plt.legend()
plt.show()

import plotly.graph_objects as go
import plotly.offline as pyo


categories = ['Food Quality', 'Food Variety', 'Service Quality', 'Ambience', 'Affordability']
categories = [*categories, categories[0]]

restaurant_1 = [4, 4, 5, 4, 3]
restaurant_2 = [5, 5, 4, 5, 2]
restaurant_3 = [3, 4, 5, 3, 5]
restaurant_1 = [*restaurant_1, restaurant_1[0]]
restaurant_2 = [*restaurant_2, restaurant_2[0]]
restaurant_3 = [*restaurant_3, restaurant_3[0]]


fig = go.Figure(
    data=[
        go.Scatterpolar(r=restaurant_1, theta=categories, fill='toself', name='Restaurant 1'),
        go.Scatterpolar(r=restaurant_2, theta=categories, fill='toself', name='Restaurant 2'),
        go.Scatterpolar(r=restaurant_3, theta=categories, fill='toself', name='Restaurant 3')
    ],
    layout=go.Layout(
        title=go.layout.Title(text='Restaurant comparison'),
        polar={'radialaxis': {'visible': True}},
        showlegend=True
    )
)

pyo.plot(fig)'''

'''try:
    type(ife)

except NameError:
    raise Exception("If is a Keyword")'''

'''from tkinter import *
from tkinter.ttk import *
 
# Create Object
root = Tk()
 
# Initialize tkinter window with dimensions 100x100            
root.geometry('100x100')    
 
btn = Button(root, text = 'Click me !',
                command = root.destroy)
 
# Set the position of button on the top of window
btn.pack(side = 'top')    
 
root.mainloop()'''

'''from jinja2 import Template

table=Template("<table>\
    <thead><tr>\
        <th>One</th>\
        <th>Two</th>\
        <th>Three</th>\
        <th>Four</th>\
    </tr></thead>\
    <tbody>\
    {% for row in tabular_data %}\
    <tr>\
        <td>{{ row.one }}</td>\
        <td>{{ row.two }}</td>\
        <td>{{ row.three }}</td>\
        <td>{{ row.four }}</td>\
    </tr>\
    {% endfor %}\
    </tbody>\
</table>")

Dict={"one":1, "two":2, "three":3, "four":4}

print(table.render(row=Dict))'''


'''Modules:
    Scipy
    Pandas
    Numpy
    Matplotlib
    Plotly
    Astropy
    jinja2'''

'''from queue import Queue

Number=int(input("Enter the Number of terms in the Fibbonacci Sequence : "))
First=int(input("Enter the First Number : "))
Second=int(input("Enter the Second Number : "))
print()
Fibb=Queue(maxsize=2)
Fibb.put(First)
Fibb.put(Second)

for x in range(Number):
    Sum=sum(Fibb.queue)
    print(Fibb.get())
    Fibb.put(Sum)'''

'''from tabulate import tabulate
  
# assign data
mydata = [["Nikhil", "Delhi"], 
          ["Ravi", "Kanpur"], 
          ["Manish", "Ahmedabad"], 
          ["Prince", "Bangalore"]]
  
# create header
head = ["Name", "City"]
  
# display table
A=tabulate(mydata, headers=head, tablefmt="fancy_grid")
print(A)'''


'''Number=Dup=int(input("Enter the Number to Count the Number of Digits : "))
Digits=0

while Number>0:
   Number//=10
   Digits+=1

print("The Number of Digits in", Dup, "is", Digits)'''

'''Number=Dup=int(input("Enter the Number to Count the Repetition of Digits : "))
Digit=int(input("Enter a Digit to calculate how many time it's repeated : "))
Rep=0

while Number>0:
   Var=Number%10

   if Var==Digit:
      Rep+=1

   Number//=10

print(Digit, "is Repeated", Rep, "times") '''

'''Charac=input("Enter a Character to check whether it is a Vowel or Consonant : ")
if len(Charac)>1:print("Please Enter a Single Character")
if Charac in ("aeiou"):print(Charac, "is a Vowel")
else:print(Charac, "is a Consonent")'''

'''Value=float(input("Enter the Value for x : "))
No=int(input("Enter the Number of terms in the Series : "))
Sum=0

for x in range(No):
   Sum+=(Value**x)

print("The Sum of the Series is :", Sum)'''

'''List=[]
for x in range(1,100):
   if x%3==0 or x%5==0:
      List.append(x)

print(List)'''

'''L=[12,15,17,13,21]

for x in range(-1, -len(L), -1):
   L[x], L[x-1]=L[x-1], L[x]
   print(L)'''

'''L=['41', 'DROND', 'GIRIRAJ', '13', 'ZARA']

for x in L:
    try:
        y=int(x)
        print(x*3)

    except:
        print(x+"#")'''

Str=input("Enter : ")
Str=Str.upper()
Vowels={}

for x in Str:
    if x in ("AEIOU"):
        if x in Vowels:
            Vowels[x]+=1

        else:
            Vowels[x]=1

print(Vowels)        
