Var=input("Enter the String:")

for x in Var:
    if 96<ord(x)<123:
        print(chr(122-(ord(x)-97)), end="")
        
    else:
        print(x, end="")


Var=input("Enter a Chemical :")

Var=Var.split()

for x in Var:
    if len(x)>1:
        print(ord(x[0])+ord(x[1]), end=" ")
        
    else:
        print(ord(x[0]))




Var1=input("Enter a String :")
Var1=list(Var1)
Var1.sort()
Num=int(input("Enter the number of words :"))
List=[]
for x in range(Num):
    List.append(input("Enter a Word:"))
    
for y in List:
    Dup=list(y)
    Dup.sort()
    if Var1==Dup:
        print(y)
        break

    
