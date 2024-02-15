'''
List=[1,1,3,4,5,7,9,10]
Dup=List[:]

for x in Dup:
    if x%2==1:
        List.remove(x)

print("The List after removing the Odd Numbers is :", List)        
'''

'''
List=[1,1,3,4,5,7,9,10]
Max=0
Second_Max=0

for x in List:
    if Max<x:
        Max=x

for y in List:
    if Max>y>Second_Max:
        Second_Max=y

print("The Second Largest Element of the given list is :", Second_Max)        
'''

'''
List=[1,1,3,4,5,7,9,10]
Cumulative=[]
Sum=0

for x in List:
    Sum+=x
    Cumulative.append(Sum)

print("The Cumulative Elements of the Given List are :", Cumulative)    
'''

'''
List=[1,2,2,1,3,4,4,2,3,1,2,3,4,3,1,2,3]
Frequency={}

for x in List:
    if x in Frequency:
        Frequency[x]+=1

    else:
        Frequency[x]=1

print("The Frequencies of the Elements of the Given List are:")

for y in Frequency:
    print(y, "-", Frequency[y])
'''

'''
List=["Arvin", "King", "aakash", "Andrew", "Ezhil"]

print("The Strings starting with 'A' in the given list are :")

for x in List:
    if x[0] in "Aa":
        print(x)
'''

'''
List=[14,2,22,33,45,43,93,73,3]
Sum=0

for x in List:
    if x%10==3:
        Sum+=x

print("The Sum of all values ending with 3 in the Given List is :", Sum)        
'''

'''
List=[-12,11,-13,-5,6,-7,5,-3,-6]
Counter=0

for x in range(len(List)-1):
    for y in range(len(List)-1-x):
        Counter+=1
        print(List)
        if List[y]<0:
            List[y], List[y+1]=List[y+1], List[y]

print("The List after shifting Negative Numbers to the Right is :", List)
print(Counter)
'''

'''
List=[2,21,3,4,28,1,7,70,6]
x=0

while x<len(List):
    if List[x]%7==0:
        List[x],List[x+1]=List[x+1],List[x]
        x+=2

    else:
        x+=1

print("The List after Swapping the Values divisible by 7 is:", List)        
'''

'''
No=int(input("Enter the Length of the Tuple : "))
Tuple=()

for x in range(1,No+1):
    Input=eval(input("Enter the Value no." + str(x) + " : "))
    Tuple+=(Input,)

print("The Tuple you created is here :", Tuple)    
'''

'''
No=int(input("Enter the Total Number of Sections in 11th Standand : "))
Info={}

for x in range(No):
    Sec=input("Enter the Section : ").upper()
    Stream=input("Enter the Stream Name : ").title()

    Info[Sec]=Stream

print("The Section and Stream name of the Classes in 11th Standard are :")

for y in Info:
    print(y, " - ", Info[y])
'''

'''
No=int(input("Enter the Total Number of Entries : "))
print()
Info={}

for x in range(No):
    Country=input("Enter the Country : ")
    Capital=input("Enter the Capital of the Country : ")
    Currency=input("Enter the Currency of the Country : ")
    print()

    Info[Country]=(Capital, Currency)

print("The Countries, their Capitals and their Currencies are : ")
print()

for y in Info:
    print(y, " - ", Info[y][0], " , ", Info[y][1])

print()
print("Searching :")
print()

Var=input("Enter the Name of the Country to search : ")
print()

if Var in Info:
    print(Var, " - ", Info[Var][0], " , ", Info[Var][1])

else:
    print("Record Not Found !")
'''

