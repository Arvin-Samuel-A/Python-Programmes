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

