def func1():
    num1=input("Enter the Position of the Element of the List which you need to Edit (from 0 to 3 and -1 to -4): ")
    ele1=input("Enter the Value of the Element which you need to Replace : ")
    print("", end="\n")
    List1[int(num1)]=ele1    

def func2():
    num1=input("Enter the Position of the First Element of the List which you need to Edit (from 0 to 3 and -1 to -4): ")
    ele1=input("Enter the Value of the Element which you need to Replace : ")
    List1[int(num1)]=ele1
    print("", end="\n")
    
    num2=input("Enter the Position of the Second Element of the List which you need to Edit (from 0 to 3 and -1 to -4): ")
    ele2=input("Enter the Value of the Element which you need to Replace : ")
    List1[int(num2)]=ele2
    print("", end="\n")
    print("The List which you have created and edited is here : ", List1)    

def func3():
    num1=input("Enter the Position of the First Element of the List which you need to Edit (from 0 to 3 and -1 to -4): ")
    ele1=input("Enter the Value of the Element which you need to Replace : ")
    List1[int(num1)]=ele1
    print("", end="\n")

    num2=input("Enter the Position of the Second Element of the List which you need to Edit (from 0 to 3 and -1 to -4): ")    
    ele2=input("Enter the Value of the Element which you need to Replace : ")
    List1[int(num2)]=ele2
    print("", end="\n")
    
    num3=input("Enter the Position of the Third Element of the List which you need to Edit (from 0 to 3 and -1 to -4): ")
    ele3=input("Enter the Value of the Element which you need to Replace : ")
    List1[int(num3)]=ele3
    print("", end="\n")
    print("The List which you have created and edited is here : ", List1)    
    
def func4():
    num1=input("Enter the Position of the First Element of the List which you need to Edit (from 0 to 3 and -1 to -4): ")
    ele1=input("Enter the Value of the Element which you need to Replace : ")
    List1[int(num1)]=ele1
    print("", end="\n")

    num2=input("Enter the Position of the Second Element of the List which you need to Edit (from 0 to 3 and -1 to -4): ")
    ele2=input("Enter the Value of the Element which you need to Replace : ")
    List1[int(num2)]=ele2
    print("", end="\n")
    
    num3=input("Enter the Position of the Third Element of the List which you need to Edit (from 0 to 3 and -1 to -4): ")
    ele3=input("Enter the Value of the Element which you need to Replace : ")
    List1[int(num3)]=ele3
    print("", end="\n")
    
    num4=input("Enter the Position of the Fourth Element of the List which you need to Edit (from 0 to 3 and -1 to -4): ")
    ele4=input("Enter the Value of the Element which you need to Replace : ")
    List1[int(num4)]=ele4
    print("", end="\n")
    print("The List which you have created and edited is here : ", List1)

def func5():
    rep1=input("Enter the Value of the Element which you need to add in the list : ")
    List1.append(rep1)
    print("", end="\n")
    print("The Final List is here : ", List1)
    print("", end="\n")
    print("THANK YOU !!")

def func6():
    pos1=input("Enter the Position where you want the new element to be added (from 0 to 3 and -1 to -4) : ")
    rep1=input("Enter the Value of the Element which you need to add in the list : ")
    List1.insert(int(pos1), rep1)
    print("", end="\n")
    print("The Final List is here : ", List1)
    print("", end="\n")
    print("THANK YOU !!")


print("We are going to Change and Add the items in the List", end="\n\n")
ListNew=["First we will enter the values to store in the List.", "Next we will change the items in the List.", "Finally we will add items to List."]
for x in ListNew:
    print(x)
print("", end="\n")

Item1=input("Enter the First Element which you need to store in the List : ")
Item2=input("Enter the Second Element which you need to store in the List : ")
Item3=input("Enter the Third Element which you need to store in the List : ")
Item4=input("Enter the Fourth Element which you need to store in the List : ")

List1=[Item1, Item2, Item3, Item4]

print("", end="\n")    
X=str(input("Do you need to change something in the List ? "))

if X=="Yes" or X=="yes" or X=="YES":
    print("", end="\n")
    Y=int(input("How many items do you need to change in the list (from 1 to 4) : "))
    print("", end="\n")

    if Y==1:
        func1()
    if Y==2:
        func2()
    if Y==3:
        func3()
    if Y==4:
        func4()

else:
    print("", end="\n")
    print("The List which you have created is here : ", List1)
    print("", end="\n")

A=str(input("Finally do you want to Add something to the List ? "))

if A=="Yes" or A=="yes" or A=="YES":
    print("", end="\n")
    B=str(input("Do you want to add the new item in the End or in a Specific Position ? "))
    print("", end="\n")

    if B=="End" or B=="end" or B=="END" :
        func5()

    else :
        func6()

else :
    print("The Final List is here : ", List1)
    print("", end="\n")
    print("THANK YOU !!")
