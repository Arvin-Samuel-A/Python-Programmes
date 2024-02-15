Entries=int(input("How mant Entries do you want to enter ? "))
Info={}

for x in range(Entries):
    Name=input("Enter the Name of the Employee : ")
    Salary=input("Enter the Salary of " + str(Name) + " : ")
    Info[Name]=Salary

print("Employee","Employee",    )
print("Name","Salary", sep="\t")

for y in Info:
    print(y, Info[y], sep="\t")

