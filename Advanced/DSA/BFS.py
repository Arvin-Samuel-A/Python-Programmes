from Advanced.DSA.Queue import Queue

def Neighbours(Adj_Mat, Value):

    Neigh=[]

    for x in range(len(Adj_Mat[Value])):

        if Adj_Mat[Value][x]:

            Neigh.append(x)

    return Neigh


def BFS_AM(Adj_Mat, Value):

    (Rows, Cols)=Adj_Mat.shape
    Visited, Parent, Level = {}, {}, {}

    for x in range(Rows):

        Visited[x]=False
        Parent[x]=-1
        Level[x]=-1

    Q=Queue()

    Visited[Value]=True
    Level[Value]=0

    Q.Put(Value)

    while (not Q.isempty()):

        Var=Q.Get()

        for y in Neighbours(Adj_Mat, Var):

            if (not Visited[y]):

                Level[y]=Level[Var]+1
                Visited[y]=True
                Parent[y]=Var
                
                Q.Put(y)

    return Visited, Parent, Level


def BFS_AL(Adj_List, Value):

    Visited, Parent, Level = {}, {}, {}

    for x in Adj_List.keys():

        Visited[x]=False
        Parent[x]=-1

    Q=Queue()

    Visited[Value]=True
    Level[Value]=0

    Q.Put(Value)

    while (not Q.isempty()):

        Var=Q.Get()

        for y in Adj_List[Var]:

            if(not Visited[y]):

                Level[y]=Level[Var]+1
                Visited[y]=True
                Parent[y]=Var

                Q.Put(y)

    return Visited, Parent, Level