print("We are going to print the prime numbers in a Particular Range", end='\n\n')
Start=int(input("Enter the Starting Number of the Range : "))
End=int(input("Enter the Ending Number of the Range : "))
Dup=Start

if Start<1:
    print("Please Enter a Positive Starting Number More than 1 !")

elif Start>End:
    print("Please Enter the Starting Number less than the Ending Number !")

elif Start==End:
    print("Please Enter different values for Starting and Ending Number !")

else: 
    if Start==1:
        Dup=Start+1
    for x in range(Dup, End+1):
        i=2
        while x>i:
            if x%i==0:
                break
            i+=1
            
        else:
            print(x)                
    else:
        print("These are the Prime Numbers from " + str(Start) + " to " + str(End))
            
