No=int(input("Enter the number to check whether it is prime or not : "))
Prime=True
i=2
while i**2 <=No :
    if No%i==0:
        Prime=False
        break
    i+=1

if Prime:
    print(No, "is a Prime Number")

else:    
    print(No, "is Divisible by", i, "and it is not a Prime Number")
