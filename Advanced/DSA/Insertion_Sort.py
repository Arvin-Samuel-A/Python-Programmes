def Insert(List, Value):

    Len=len(List)

    if (Len==0):

        return [Value]
    
    if Value>=List[-1]:

        return(List+[Value])
    
    else:

        return Insert(List[:-1], Value) + [List[-1]]
    
def Insertion_Sort(List):

    Len=len(List)

    if Len<1:

        return List
    
    List=Insert(Insertion_Sort(List[:-1]), List[-1])

    return List


if __name__=="__main__":
       
    List=eval(input("Enter the List of Elements to be Sorted : "))

    print()

    print("The Sorted List is : ", Insertion_Sort(List))