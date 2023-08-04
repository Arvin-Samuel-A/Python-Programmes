No=int(input("Enter how many values do you need for the Fibonacci Series : "))
Counter=2

if No<=1:
    No1=int(input("Enter the First Number for the Series : "))
    print(No1)

elif No<=2:
    No1=int(input("Enter the First Number for the Series : "))
    No2=int(input("Enter the Second Number for the Series : "))
    print(No1)
    print(No2)
    
else:
    No1=int(input("Enter the First Number for the Series : "))
    No2=int(input("Enter the Second Number for the Series : "))
    Num1=No1
    Num2=No2
    print(No1)
    print(No2)
    while Counter<No :
        FC=No1+No2
        print(FC)
        No1=No2
        No2=FC
        Counter+=1
        
print("")
print("The Fibonacci Series till " + str(No) + " between " + str(Num1) + " and " + str(Num2) + " is given above !!")
