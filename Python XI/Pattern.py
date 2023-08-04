#Increasing Step
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end='')
    print('')

#Decreasing Step
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end='')
    print('')            

#Floyd's Triangle
n=int(input("Enter the Starting Number : "))
for i in range(n, 0, -1):
    for j in range(n, i-1, -1):
        print(j, end='')
    print('')    
