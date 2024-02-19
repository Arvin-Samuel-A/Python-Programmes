def Quick_Sort(List, Start, End):

    if (End-Start<=1):

        return List
    
    Pivot=List[Start]
    Lower=Upper=Start+1

    for x in range(Start+1, End):

        if (List[x]>Pivot):

            Upper+=1

        else:

            List[x], List[Lower] = List[Lower], List[x]

            Lower+=1
            Upper+=1

    List[Start], List[Lower-1] = List[Lower-1], List[Start]
    Lower-=1

    Quick_Sort(List, Start, Lower)
    Quick_Sort(List, Lower+1, Upper)

    return List


List=eval(input("Enter the List of Elements to be Sorted : "))

print()

print("The Sorted List is : ", Quick_Sort(List, 0, len(List)))