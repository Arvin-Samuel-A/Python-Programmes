Num=int(input("Enter a Number to whether it's a Perfect Number or not : "))
Factors=0
i=1
while i<Num :
    if Num%i==0:
        Factors+=i
    i+=1

if Factors==Num:
    print("The Entered Number of " + str(Num) + " is a Perfect Number ")

else:
    print("The Entered Number of " + str(Num) + " is not a Perfect Number ")
        
