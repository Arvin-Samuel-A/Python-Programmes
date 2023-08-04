print("We are going to find the sum of the series 1 + x/1! + x^2/2!...x^n/n!", end='\n\n')
Value=float(input("Enter the value of 'x' : "))
Limit=int(input("Enter the Number of terms in the Series : "))
Sum=1

for x in range(Limit+1):
    Fact=1
    for y in range(1, x+1):
        Fact*=y
    Sum+=(Value**x)/Fact

print("The Sum of the Series till " + str(Limit) + " with 'x' as " + str(Value) + " is equal to", Sum)

        
