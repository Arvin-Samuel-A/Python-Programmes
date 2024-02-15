Sec=int(input("For how many sections do you want to enter the details ? "))
Info={}
print()

for x in range(Sec):
    Class_Sec=input("Enter the Class and the Section : ").upper()
    Stream=input("Enter the Stream Name (Science, Commerce, Humanities or Allen) : ").capitalize()
    Info[Class_Sec]=Stream

for y in Info:
    print(y, "-", Info[y])
    
