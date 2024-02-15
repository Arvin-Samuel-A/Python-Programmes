Num=int(input("Enter the Number which you want to reverse : "))
Rev=0
Num2=Num
while Num > 0:
    Rem=Num%10
    Rev=Rev*10+Rem
    Num//=10
print("The Reverse of " + str(Num2) + " is " ,Rev)    
    
