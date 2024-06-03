def Merge_Count(List1 : list, List2 : list):

    Len1 = len(List1)
    Len2 = len(List2)

    List3 = []

    x = y = z = 0
    Count = 0

    while(z < Len1+Len2):

        if(x == Len1):

            List3.append(List2[y])

            y += 1
            z += 1

        elif(y == Len2):

            List3.append(List1[x])

            x += 1
            z += 1

        elif(List1[x] < List2[y]):

            List3.append(List1[x])

            x += 1
            z += 1

        else:

            List3.append(List2[y])

            y += 1
            z += 1
            Count += (Len1 - x)

    return List3, Count

def Sort_Count(List : list):

    Len = len(List)

    if (Len == 1):

        return(List, 0)
    
    (Left, Count_Left) = Sort_Count(List[:Len//2])
    (Right, Count_Right) = Sort_Count(List[Len//2:])
    
    (Result, Count_Final) = Merge_Count(Left, Right)

    return (Result, Count_Left+Count_Right+Count_Final)

