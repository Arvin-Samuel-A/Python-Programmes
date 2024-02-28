import numpy as np
from Queue import *

def Topological_Sorting_AM(Adj_Mat : np.array):

    In_Degree={}
    Sort_List=[]
    Longest_Path={}

    (Rows, Cols) = Adj_Mat.shape

    for x in range(Cols):

        In_Degree[x]=0
        Longest_Path[x]=0

        for y in range(Rows):

            if Adj_Mat[y, x]==1:

                In_Degree[x]+=1

    Zero_In=Queue()

    for x in range(Rows):

        if (In_Degree[x]==0):

            Zero_In.Put(x)

    while(not Zero_In.isempty()):

        Start=Zero_In.Get()
        Sort_List.append(Start)

        In_Degree[Start]-=1

        for y in range(Cols):

            if (Adj_Mat[Start, y]==1):

                In_Degree[y]-=1
                Longest_Path[y]=max(Longest_Path[y], Longest_Path[Start]+1)

                if (In_Degree[y]==0):

                    Zero_In.Put(y)

    return Sort_List, Longest_Path


def Topological_Sorting_AL(Adj_List : dict):

    In_Degree={}
    Sort_List=[]
    Longest_Path={}

    for x in Adj_List.keys():

        In_Degree[x]=0
        Longest_Path[x]=0

    for x in Adj_List.keys():

        for y in Adj_List[x]:

            In_Degree[y]+=1

    Zero_In=Queue()

    for x in Adj_List:

        if (In_Degree[x]==0):

            Zero_In.Put(x)

    while(not Zero_In.isempty()):

        Start=Zero_In.Get()
        Sort_List.append(Start)

        In_Degree[Start]-=1

        for x in Adj_List[Start]:

            In_Degree[x]-=1
            Longest_Path[x]=max(Longest_Path[x], Longest_Path[Start]+1)

            if (In_Degree[x]==0):

                Zero_In.Put(x)
    
    return Sort_List, Longest_Path


Adj_Mat = np.array([
    [0, 1, 1, 0, 0, 0],  # Node 0
    [0, 0, 0, 1, 0, 0],  # Node 1
    [0, 0, 0, 0, 1, 0],  # Node 2
    [0, 0, 0, 0, 0, 1],  # Node 3
    [0, 0, 0, 0, 0, 1],  # Node 4
    [0, 0, 0, 0, 0, 0]   # Node 5
])

print(Topological_Sorting_AM(Adj_Mat))

Adj_List={
    0: [1, 2],
    1: [3],
    2: [4],
    3: [5],
    4: [5],
    5: []
}

print(Topological_Sorting_AL(Adj_List))