import numpy as np

Visited, Parent, Level = {}, {}, {}

def Neighbours(Adj_Mat : np.array, Value : int):

    Neigh=[]

    for x in range(len(Adj_Mat[Value])):

        if Adj_Mat[Value][x]:

            Neigh.append(x)

    return Neigh


def DFS_AM_Initialization(Adj_Mat : np.array, Start : int):

    (Rows, Cols) = Adj_Mat.shape

    for x in range(Rows):

        Visited[x]=False
        Parent[x]=-1
        Level[x]=-1

    Level[Start]=0

    return


def DFS_AL_Initialization(Adj_List : dict, Start : int):

    for x in Adj_List.keys():

        Visited[x]=False
        Parent[x]=-1
        Level[x]=-1

    Level[Start]=0

    return


def DFS_AM(Adj_Mat : np.array, Start : int):

    global Visited, Parent, Level

    Visited[Start]=True

    for x in Neighbours(Adj_Mat, Start):

        if (not Visited[x]):

            Parent[x]=Start
            Level[x]=Level[Start]+1

            DFS_AM(Adj_Mat, x)

    return


def DFS_AL(Adj_List : dict, Start : int):

    global Visited, Parent, Level

    Visited[Start]=True

    for x in Adj_List[Start]:

        if (not Visited[x]):

            Parent[x]=Start
            Level[x]=Level[Start]+1

            DFS_AL(Adj_List, x)

    return


Adj_Mat = np.array([
    [0, 1, 1, 1, 0], # Node 0
    [1, 0, 0, 0, 0], # Node 1
    [1, 0, 0, 1, 1], # Node 2
    [1, 0, 1, 0, 0], # Node 3
    [0, 0, 1, 0, 0]  # Node 4
])

DFS_AM_Initialization(Adj_Mat, 0)
DFS_AM(Adj_Mat, 0)

print(Visited, Parent, Level)

Adj_List={
    0:[1, 2, 3], 
    1:[0], 
    2:[0, 3, 4], 
    3:[0, 2], 
    4:[2]
}

DFS_AL_Initialization(Adj_List, 0)
DFS_AL(Adj_List, 0)

print(Visited, Parent, Level)