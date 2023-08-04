def power(n):
    return lambda a: a**n
print("We are going to find n'th power of the entered term",end='\n\n')
Num1=float(input("Enter the Number which you want to find the power of : "))
Num2=float(input("Enter the number to which to want to raise the previous entered number: "))

Pow1=power(Num2)
print("The " + str(Num1) + " raised to the power of "  + str(Num2) + " is : ", Pow1(Num1))
