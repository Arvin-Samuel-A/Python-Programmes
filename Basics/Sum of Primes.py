Num2=int(input("Enter the Ending Number : "))

Sum=2

for x in range(3,Num2+1):
    if x%2==0:
        continue

    else:
        Var=x//2

        for y in range(3,Var,2):
            if x%y==0:
                break

        else:
            Sum +=x

print("Sum : ", Sum)
