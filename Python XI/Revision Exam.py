'''Number=int(input("Enter a Number : ")[::-1])
Text=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

while Number>0:
    var=Number%10
    print(Text[var], end=" ")
    Number//=10'''


'''Number=input("Enter a Number : ")
Text=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for x in Number:
    print(Text[int(x)], end=" ")'''


'''Num=int(input("Enter a Number to create a Pattern : "))

for i in range(Num, 0 , -1):
    for j in range(Num, i-1, -1):
        print(j, end=" ")
    print()'''    


'''def Factorial(Number):
    Fact=1
    for x in range(1, Number+1):
        Fact*=x
    return Fact'''

Value=int(input("Enter the Value of x :"))
Num=int(input("Enter the Number of terms : "))
Sum=0

for i in range(1, Num+1):
    Fact=1
    for x in range(1, i+1):
        Fact*=x
    Sum+=(Value**i)/Fact
    Sum*=-1

print("The Sum of Series : ", Sum)    


'''from queue import LifoQueue as Stack

S=Stack()
N=[12, 13, 34, 56, 21, 79, 98, 22, 35, 38]

for x in N:
    if x%2==0:
        S.put(x)

for y in range(S.qsize()):
    print(S.get(), end=" ")'''

'''S=[]
N=[12, 13, 34, 56, 21, 79, 98, 22, 35, 38]

for x in N:
    if x%2==0:
        S.append(x)

for y in range(len(S)):
    print(S.pop(), end=" ")'''
