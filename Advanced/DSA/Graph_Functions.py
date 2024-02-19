from BFS import *

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