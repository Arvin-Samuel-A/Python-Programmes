from copy import deepcopy

class Max_Heap:

    def __init__(self, Elements : list):

        self.Heap = Elements
        self.Length = len(Elements)
        self.Max = self.Length

        self.Element_to_Heap_Position = {}
        self.Heap_Position_to_Element = {}

        for x in range(self.Length):

            self.Element_to_Heap_Position[x]=x
            self.Heap_Position_to_Element[x]=x

        self.Build()

        return
    

    def Top_Heapify(self, Heap_Position : int):

        Largest = Heap_Position
        Left = 2 * Heap_Position + 1
        Right = 2 * Heap_Position + 2

        if (Left<self.Length and self.Heap[Left]>self.Heap[Largest]):

            Largest=Left

        if (Right<self.Length and self.Heap[Right]>self.Heap[Largest]):

            Largest=Right

        if (Largest!=Heap_Position):

            self.Swap(Heap_Position, Largest)

            self.Top_Heapify(Largest)

        return


    def Bottom_Heapify(self, Heap_Position : int):

        Parent=(Heap_Position-1)//2

        if (Parent>=0):

            if (self.Heap[Heap_Position]>self.Heap[Parent]):

                self.Swap(Heap_Position, Parent)

                self.Bottom_Heapify(Parent)

        return
    

    def Insert(self, Element : int):

        self.Heap.append(Element)
        self.Length+=1

        New=self.Max
        self.Max+=1

        self.Element_to_Heap_Position[New]=self.Length-1
        self.Heap_Position_to_Element[self.Length-1]=New

        self.Bottom_Heapify(self.Length-1)

        return
    

    def Delete(self):

        self.Swap(0, self.Length-1)

        Temp=self.Heap_Position_to_Element[self.Length-1]

        del self.Element_to_Heap_Position[Temp]
        del self.Heap_Position_to_Element[self.Length-1]

        self.Length-=1
        
        self.Top_Heapify(0)

        return self.Heap.pop()
    
    
    def Update(self, Element : int, New_Value : int):

        Index=self.Element_to_Heap_Position[Element]
        self.Heap[Index]=New_Value

        if(New_Value > self.Heap[(Index-1)//2] and Index!=0):

            self.Bottom_Heapify(Index)

            return
        
        self.Top_Heapify(Index)

        return
    

    def Sort(self, reverse=False):

        Temp1=deepcopy(self.Heap)
        Temp2=self.Length

        while(self.Length>1):

            self.Heap[0], self.Heap[self.Length-1] = self.Heap[self.Length-1], self.Heap[0]
            self.Length-=1

            self.Top_Heapify(0)    

        self.Heap, Temp1 = Temp1, self.Heap
        self.Length=Temp2

        if (reverse):

            return Temp1[::-1]
        
        return Temp1
    

    def Build(self):

        Mid = self.Length//2-1

        for x in range(Mid, -1, -1):

            self.Top_Heapify(x)

        return
    

    def Swap(self, Heap_Position1 : int, Heap_Position2 : int):

        Temp1=self.Heap_Position_to_Element[Heap_Position1]
        Temp2=self.Heap_Position_to_Element[Heap_Position2]

        self.Element_to_Heap_Position[Temp1], self.Element_to_Heap_Position[Temp2] = self.Element_to_Heap_Position[Temp2], self.Element_to_Heap_Position[Temp1]
        self.Heap_Position_to_Element[Heap_Position1], self.Heap_Position_to_Element[Heap_Position2] = self.Heap_Position_to_Element[Heap_Position2], self.Heap_Position_to_Element[Heap_Position1]
        
        self.Heap[Heap_Position1], self.Heap[Heap_Position2] = self.Heap[Heap_Position2], self.Heap[Heap_Position1]

        return
    

    def __str__(self):

        return str(self.Heap)


class Min_Heap:

    def __init__(self, Elements : list):

        self.Heap = Elements
        self.Length = len(Elements)
        self.Max = self.Length

        self.Element_to_Heap_Position = {}
        self.Heap_Position_to_Element = {}

        for x in range(self.Length):

            self.Element_to_Heap_Position[x]=x
            self.Heap_Position_to_Element[x]=x

        self.Build()

        return
        

    def Top_Heapify(self, Heap_Position : int):

        Smallest = Heap_Position
        Left = 2 * Heap_Position + 1
        Right = 2 * Heap_Position + 2

        if (Left<self.Length and self.Heap[Left]<self.Heap[Smallest]):

            Smallest=Left

        if (Right<self.Length and self.Heap[Right]<self.Heap[Smallest]):

            Smallest=Right

        if (Smallest!=Heap_Position):

            self.Swap(Heap_Position, Smallest)

            self.Top_Heapify(Smallest)

        return


    def Bottom_Heapify(self, Heap_Position : int):

        Parent=(Heap_Position-1)//2

        if (Parent>=0):

            if (self.Heap[Heap_Position]<self.Heap[Parent]):

                self.Swap(Heap_Position, Parent)

                self.Bottom_Heapify(Parent)

        return


    def Insert(self, Element : int):

        self.Heap.append(Element)
        self.Length+=1

        New=self.Max
        self.Max+=1

        self.Element_to_Heap_Position[New]=self.Length-1
        self.Heap_Position_to_Element[self.Length-1]=New

        self.Bottom_Heapify(self.Length-1)

        return
    

    def Delete(self):

        self.Swap(0, self.Length-1)

        Temp=self.Heap_Position_to_Element[self.Length-1]

        del self.Element_to_Heap_Position[Temp]
        del self.Heap_Position_to_Element[self.Length-1]

        self.Length-=1
        
        self.Top_Heapify(0)

        return self.Heap.pop()
    
    
    def Update(self, Element : int, New_Value : int):

        Index=self.Element_to_Heap_Position[Element]
        self.Heap[Index]=New_Value

        if(New_Value < self.Heap[(Index-1)//2] and Index!=0):

            self.Bottom_Heapify(Index)

            return
        
        self.Top_Heapify(Index)

        return
    

    def Sort(self, reverse=False):

        Temp1=deepcopy(self.Heap)
        Temp2=self.Length

        while(self.Length>1):

            self.Heap[0], self.Heap[self.Length-1] = self.Heap[self.Length-1], self.Heap[0]
            self.Length-=1

            self.Top_Heapify(0)    

        self.Heap, Temp1 = Temp1, self.Heap
        self.Length=Temp2

        if (reverse):

            return Temp1
        
        return Temp1[::-1]



    def Build(self):

        Mid = self.Length//2-1

        for x in range(Mid, -1, -1):

            self.Top_Heapify(x)

        return
    

    def Swap(self, Heap_Position1 : int, Heap_Position2 : int):

        Temp1=self.Heap_Position_to_Element[Heap_Position1]
        Temp2=self.Heap_Position_to_Element[Heap_Position2]

        self.Element_to_Heap_Position[Temp1], self.Element_to_Heap_Position[Temp2] = self.Element_to_Heap_Position[Temp2], self.Element_to_Heap_Position[Temp1]
        self.Heap_Position_to_Element[Heap_Position1], self.Heap_Position_to_Element[Heap_Position2] = self.Heap_Position_to_Element[Heap_Position2], self.Heap_Position_to_Element[Heap_Position1]
        
        self.Heap[Heap_Position1], self.Heap[Heap_Position2] = self.Heap[Heap_Position2], self.Heap[Heap_Position1]

        return


    def __str__(self):

        return str(self.Heap)



if __name__=="__main__":

    Heap=Min_Heap([1, 2, 3, 4, 8, 5, 6, 7])

    print(Heap)
    print(Heap.Element_to_Heap_Position)
    print(Heap.Heap_Position_to_Element)
    print()

    print(Heap.Delete())

    print(Heap)
    print(Heap.Element_to_Heap_Position)
    print(Heap.Heap_Position_to_Element)
    print()

    Heap.Insert(90)

    print(Heap)
    print(Heap.Element_to_Heap_Position)
    print(Heap.Heap_Position_to_Element)
    print()

    Heap.Update(9, 67)
    print(Heap)
    print(Heap.Element_to_Heap_Position)
    print(Heap.Heap_Position_to_Element)
    print()

    print(Heap.Sort())