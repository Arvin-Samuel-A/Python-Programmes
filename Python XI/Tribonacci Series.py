No=int(input("Enter the value till which you need to print the Tribonacci Series : "))
Counter=3

if No<=1 :
    No1=int(input("Enter the First Number for the Series : "))
    print(No1)
    

elif No<=2 :
    No1=int(input("Enter the First Number for the Series : "))
    No2=int(input("Enter the Second Number for the Series : "))
    print(No1)
    print(No2)
    

elif No<=3 :
    No1=int(input("Enter the First Number for the Series : "))
    No2=int(input("Enter the Second Number for the Series : "))
    No3=int(input("Enter the Third Number for the Series : "))
    print(No1)
    print(No2)
    print(No3)

else:
    No1=int(input("Enter the First Number for the Series : "))
    No2=int(input("Enter the Second Number for the Series : "))
    No3=int(input("Enter the Third Number for the Series : "))    
    print(No1)
    print(No2)
    print(No3)
    
    while Counter<No:
        TC=No1+No2+No3
        print(TC)
        No1=No2
        No2=No3
        No3=FC
        Counter+=1

print("")
print("The Tribonacci Series till " + str(No) + " is given above !!")    
