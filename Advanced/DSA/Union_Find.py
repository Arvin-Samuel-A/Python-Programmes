class Union_Find:

    def __init__(self, Vertices):

        self.__Component={}
        self.__Members={}
        self.__Size={}

        for x in Vertices:

            self.__Component[x]=x
            self.__Members[x]=[x]
            self.__Size[x]=1

        return

    def find(self, Vertex):

        return self.__Component[Vertex]
    
    def union(self, Vertex1, Vertex2):

        self.__Comp_Old=self.__Component[Vertex1]
        self.__Comp_New=self.__Component[Vertex2]

        if (self.__Size[self.__Comp_Old]>self.__Size[self.__Comp_New]):

            self.__Comp_New, self.__Comp_Old = self.__Comp_Old, self.__Comp_New

        for x in self.__Members[self.__Comp_Old]:

            self.__Component[x]=self.__Comp_New
            self.__Members[self.__Comp_New].append(x)
            self.__Size[self.__Comp_New]+=1

        return

