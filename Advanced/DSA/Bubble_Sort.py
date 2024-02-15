def Bubble_Sort(List, Len):

    Swapped=False

    for y in range(Len-1):

        if (List[y]>List[y+1]):

            List[y], List[y+1] = List[y+1], List[y]
            Swapped=True

    if (not Swapped):

        return List

    return Bubble_Sort(List, Len-1)


List=eval(input("Enter the List of Elements to be Sorted : "))
Len=len(List)

print()

print("The Sorted List is : ", Bubble_Sort(List, Len))