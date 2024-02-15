Num1=int(input("Enter a number to check whether it's Armstrong or not : "))
var=Num1
Num2=0
while Num1>0:
    temp=Num1
    Num1=Num1%10
    Num2+=(Num1**3)
    Num1=temp//10

if Num2==var:
    print("The Entered Number of " + str(var) + " is an Armstrong Number")

else:
    print("The Entered Number of " + str(var) + " is not an Armstrong Number")
