#14

'''
Given=[14,25,67,55,32,31,98,73,21,59]
Dup=Given[:]

for x in Dup:
    if x%2==1:
        Given.remove(x)

print("The Original List is : ", Dup)
print("The List after removing the Odd Numbers is : ", Given)
'''

#15

'''
Given=[14,25,67,55,32,31,98,73,21,59]
Max=Second=0

for x in Given:
    if x>Max:
        Max=x

for y in Given:
    if Second<y<Max:
        Second=y

print("The Given List is : ", Given)
print("The Second Highest Value in the List is : ", Second)
'''

#16

'''
Given=[14,25,67,55,32,31,98,73,21,59]
CF=[]
Cumulative=0

for x in Given:
    Cumulative+=x
    CF.append(Cumulative)

print("The Given List is : ", Given)
print("The List with Cumulative Elements of the given list is : ", CF) 
'''

#17

'''
Given=eval(input("Enter a List to calculate the Frequency of various elements : "))
Frequency={}

for x in Given:
    if x in Frequency:
        Frequency[x]=Frequency[x]+1
        continue
    
    Frequency[x]=1


print("The Frequency of the Elements of the entered list are : ")

for y in Frequency:
    print(y, '-', Frequency[y])
'''

#18

'''
Given=["Arvin","Ezhil","andrew","Kingston","Sai","arv"]
Counter=0

for x in Given:
    if x[0]=='a' or x[0]=='A':
        print(x)
        Counter+=1

print("So there are", Counter, "Strings starting with the Letter 'A'")    
'''

#19

'''
Given=[13,25,63,55,32,31,93,73,21,53]
Sum=0

for x in Given:
    if x%10==3:
        Sum+=x

print("The Given List is : ", Given)
print("The Sum of the Elements ending with 3 is :", Sum)
'''

#20

'''
Given=eval(input("Enter a List to shift -ve Numbers to the Left and +ve Numbers to the Right : "))
print("The Original List is : ", Given)

for x in range(len(Given)-1):
    for y in range(len(Given)-1-x):
        if Given[y]>0:
            Given[y],Given[y+1]=Given[y+1],Given[y]

print("The Final List after shifting the Numbers are : ", Given)
'''

#21

'''
Given=eval(input("Enter a List to swap the Number divisible by 7 to the next one : "))
print("The Original List is : ", Given)
Index=0

while Index<len(Given):
    if Given[Index]%7==0:
        Given[Index],Given[Index+1]=Given[Index+1],Given[Index]
        Index+=2

    else:
        Index+=1
    
print("The Final List after shifting the Numbers are : " ,Given)        
'''

#22

'''
Number=int(input("How many values do you want to enter in the Tuple? "))
Tuple=()

for x in range(Number):
    Value=eval(input("Enter the Value No." + str(x+1) + " : "))
    Tuple+=(Value,)

print("The Final Tuple is : ", Tuple)
'''    

#23

'''
Number=int(input("For how many Sections in 11th do you want to enter the Details? "))
print()
Class_Info={}

for x in range(Number):
    Class=input("Enter the Section of 11th Standard : ").upper()
    Stream=int(input("Enter the Stream of 11-" + Class + " (1 - Science, 2 - Commerce, 3 - Humanities or 4 - Allen) : "))
    print()

    if Stream==1:
        Class_Info[Class]="Science"
        
    elif Stream==2:
        Class_Info[Class]="Commerce"

    elif Stream==3:
        Class_Info[Class]="Humanities"

    elif Stream==4:
        Class_Info[Class]="Allen"
        
    else:
        print("Please Enter any Value from 1 to 4 !")

for y in Class_Info:
    print(y, "\t-\t", Class_Info[y])
'''

#24

'''
Number=int(input("For how many Countries do you want to enter the Details? "))
print()
Countries_Info={}

for x in range(Number):
    Country=input("Enter the Name of the Country : ")
    Capital=input("Enter the Capital of " + Country + " : ")
    Currency=input("Enter the Currency of " + Country + " : ")
    print()
    
    Countries_Info[Country]=(Capital,Currency)

print("Name of the Country", "Capital of the Nation", "Currency of the Nation", sep="\t\t")

for y in Countries_Info:
    print(y + "\t\t\t\t" + Countries_Info[y][0] + "\t\t\t\t" + Countries_Info[y][1])

print()
print("Searching : ")
print()

Method=int(input("How do you want to Search (1 - Name, 2 - Capital, 3 - Currency) ? "))

if Method==1:
    Country=input("Enter the Name of the Country : ")

    if Country in Countries_Info:
        print()
        print("Details : ")
        print()
        print("Name of the Country", "Capital of the Nation", "Currency of the Nation", sep="\t\t")
        print(Country + "\t\t\t\t" + Countries_Info[Country][0] + "\t\t\t\t" + Countries_Info[Country][1])

    else:
        print("Record not Found!")

elif Method==2:
    Capital=input("Enter the Capital of the Country : ")
    
    for x in Countries_Info: 
        if Capital==Countries_Info[x][0]:
            print()
            print("Details : ")
            print()
            print("Name of the Country", "Capital of the Nation", "Currency of the Nation", sep="\t\t")
            print(x + "\t\t\t\t" + Countries_Info[x][0] + "\t\t\t\t" + Countries_Info[x][1])
            break

    else:
        print("Record not Found!")

elif Method==3:
    Currency=input("Enter the Currency of the Country : ")
    
    for x in Countries_Info: 
        if Currency==Countries_Info[x][1]:
            print()
            print("Details : ")
            print()
            print("Name of the Country", "Capital of the Nation", "Currency of the Nation", sep="\t\t")
            print(x + "\t\t\t\t" + Countries_Info[x][0] + "\t\t\t\t" + Countries_Info[x][1])
            break
    else:
        print("Record not Found!")
        
else:
    print("Please Enter any Value from 1 to 3 !")
'''
