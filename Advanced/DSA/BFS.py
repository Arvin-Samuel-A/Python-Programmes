import numpy as np
from Queue import Queue

Visited, Parent, Level = {}, {}, {}

def BFS_AM_Initialization(Adj_Mat : np.array):

    (Rows, Cols)=Adj_Mat.shape
    

    for x in range(Rows):

        Visited[x]=False
        Parent[x]=-1
        Level[x]=-1

    return


def BFS_AL_Initialization(Adj_List : dict):

    for x in Adj_List.keys():

        Visited[x]=False
        Parent[x]=-1
        Level[x]=-1

    return


def BFS_AM(Adj_Mat : np.array, Start : int):

    BFS_AM_Initialization(Adj_Mat)

    Q=Queue()

    Visited[Start]=True
    Level[Start]=0

    Q.Put(Start)

    while (not Q.isempty()):

        Var=Q.Get()

        for y in Visited:

            if (Adj_Mat[Var, y] and not Visited[y]):

                Level[y]=Level[Var]+1
                Visited[y]=True
                Parent[y]=Var
                
                Q.Put(y)

    return Visited, Parent, Level


def BFS_AL(Adj_List : dict, Start : int):

    BFS_AL_Initialization(Adj_List)

    Q=Queue()

    Visited[Start]=True
    Level[Start]=0

    Q.Put(Start)

    while (not Q.isempty()):

        Var=Q.Get()

        for y in Adj_List[Var]:

            if(not Visited[y]):

                Level[y]=Level[Var]+1
                Visited[y]=True
                Parent[y]=Var

                Q.Put(y)

    return Visited, Parent, Level


if __name__=="__main__":
    
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