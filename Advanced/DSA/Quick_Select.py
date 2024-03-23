def Median_Of_Medians(List : list):

    Len = len(List)

    if (Len <= 5):

        List.sort()
        
        return List[Len//2]
    
    Medians = []

    for x in range(0, Len, 5):

        Var = List[x : x+5]
        Var.sort()

        Medians.append(Var[len(Var)//2])

    return Median_Of_Medians(Medians)


def Quick_Select(List : list, Start : int, End : int, K : int):

    if (K < 1 or K > End-1):

        return None
    
    Pivot = Median_Of_Medians(List[Start : End])
    Pivot_Pos = 0
    
    for x in range(Start, End):

        if (List[x] == Pivot):

            Pivot_Pos = x
            break

    List[Start], List[Pivot_Pos] = List[Pivot_Pos], List[Start]
    
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

    if (K <= Lower-1):

        return Quick_Select(List, Start, Lower, K)
    
    elif (K == Lower):

        return List[Lower]
    
    else:

        return Quick_Select(List, Lower+1, End, K-Lower)