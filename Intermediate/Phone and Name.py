Entries=int(input("How many Entries do you want to enter ? "))
Info={}
print()

for x in range(Entries):
    Name=input("Enter the Name of the Person : ")
    Phone=input("Enter the Phone Number of " +str(Name) + " : ")
    Info[Name]=Phone
    print()

Search=input("Enter the Name of the person to search for the Phone Number : ")

if Search in Info:
    print("The Phone Number of", Search, "is", Info[Search])

else:
    print("There is no entry in name of", Search)
