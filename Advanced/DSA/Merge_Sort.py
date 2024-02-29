def Merge(List1, List2):

    Len1=len(List1)
    Len2=len(List2)

    List3=[]
    x=y=z=0

    while (z<Len1+Len2):

        if (x==Len1):

            List3+=List2[y:]
            z+=(Len2-y)

        elif (y==Len2):

            List3+=List1[x:]
            z+=(Len2-x)

        elif List1[x]<List2[y]:

            List3+=[List1[x]]

            x+=1
            z+=1

        else:

            List3+=[List2[y]]

            y+=1
            z+=1

    return List3

def Merge_Sort(List):

    Len=len(List)

    if Len<=1:

        return List
    
    Left=Merge_Sort(List[:Len//2])
    Right=Merge_Sort(List[Len//2:])

    Result=Merge(Left, Right)

    return Result


if __name__=="__main__":
   
    List=eval(input("Enter the List of Elements to be Sorted : "))

    print()

    print("The Sorted List is : ", Merge_Sort(List))