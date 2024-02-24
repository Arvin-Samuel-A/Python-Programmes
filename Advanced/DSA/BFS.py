import numpy as np
from Queue import Queue

Visited, Parent, Level = {}, {}, {}

def Neighbours(Adj_Mat : np.array, Value : int):

    Neigh=[]

    for x in range(len(Adj_Mat[Value])):

        if Adj_Mat[Value][x]:

            Neigh.append(x)

    return Neigh

def BFS_AM_Initialization(Adj_Mat : np.array):

    (Rows, Cols)=Adj_Mat.shape
    

    for x in range(Rows):

        Visited[x]=False
        Parent[x]=-1
        Level[x]=-1


def BFS_AM(Adj_Mat : np.array, Value : int):

    BFS_AM_Initialization(Adj_Mat)

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

    return


def BFS_Al_Initialization(Adj_List : dict):

    for x in Adj_List.keys():

        Visited[x]=False
        Parent[x]=-1
        Level[x]=-1


def BFS_AL(Adj_List : dict, Value : int):

    BFS_Al_Initialization(Adj_List)

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

    return


Adj_Mat = np.array([
    [0, 1, 1, 1, 0], # Node 0
    [1, 0, 0, 0, 0], # Node 1
    [1, 0, 0, 1, 1], # Node 2
    [1, 0, 1, 0, 0], # Node 3
    [0, 0, 1, 0, 0]  # Node 4
])

BFS_AM(Adj_Mat, 0)
print(Visited, Parent, Level)

Adj_List={
    0:[1, 2, 3], 
    1:[0], 
    2:[0, 3, 4], 
    3:[0, 2], 
    4:[2]
}

BFS_AL(Adj_List, 0)
print(Visited, Parent, Level)