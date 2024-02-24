from BFS import *

Visited, Pre, Post = {}, {}, {}

def Components(Adj_List : dict):

    Comp={}

    for x in Adj_List.keys():

        Comp[x]=-1

    Comp_Id = Seen = 0
    Max=max(Adj_List.keys())

    while (Seen<=Max):

        Start=min([x for x in Adj_List.keys() if Comp[x]==-1])

        Visited=BFS_AL(Adj_List, Start)[0]

        for x in Visited.keys():

            if Visited[x]:

                Seen+=1
                Comp[x]=Comp_Id

        Comp_Id+=1

    return Comp

def DFS_Pre_Post_Initialization(Adj_List : dict):

    for x in Adj_List.keys():

        Visited[x]=False
        Pre[x]=-1
        Post[x]=-1

    return

def DFS_Pre_Post(Adj_List : dict, Value : int, Count : int):

    Visited[Value]=True
    Pre[Value]=Count
    Count+=1

    for x in Adj_List[Value]:

        if (not Visited[x]):

            Count=DFS_Pre_Post(Adj_List, x, Count)

    Post[Value]=Count
    Count+=1

    return Count