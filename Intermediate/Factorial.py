Fac=int(input("Enter the Number for which you need to find the Factorial : "))
No=int(input("Enter the Number of Factorials to be calculated : "))
F=1
def Factorial(Number):
    global F
    for x in range(1,Number):
        F*=x
    return F

Fa=Factorial(Factorial(Factorial(Fac)))

print("The Factorial of " + str(Fac) + " is", Fa)

    
