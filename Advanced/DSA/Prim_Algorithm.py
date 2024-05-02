import numpy as np

Visited, Distance, Neighbour = {}, {}, {}

def Closest_Neighbour():

    Min=float("inf")
    Closest=None

    for x in Visited:

        Dis=Distance[x]

        if (Dis<Min and not Visited[x]) :

            Min=Dis
            Closest=x

    return Closest


def WAM_Initialize(W_Adj_Mat : np.ndarray):

    (Rows, Cols, x)=W_Adj_Mat.shape

    for x in range(Rows):

        Visited[x]=False
        Distance[x]=float("inf")
        Neighbour[x]=-1

    Visited[0]=True

    for x in range(len(W_Adj_Mat)):

        if (W_Adj_Mat[0, x, 0]):

            Distance[x]=W_Adj_Mat[0, x, 1]
            Neighbour[x]=0

    return


def WAL_Initialize(W_Adj_List : dict):

    for x in W_Adj_List.keys():

        Visited[x]=False
        Distance[x]=float("inf")
        Neighbour[x]=-1

    Visited[0]=True

    for v, w in W_Adj_List[0]:

        Distance[v]=w
        Neighbour[v]=0

    return


def Prim_Algorithm_WAM(W_Adj_Mat : np.ndarray):

    WAM_Initialize(W_Adj_Mat)

    Closest=Closest_Neighbour()

    while(Closest is not None):

        Visited[Closest]=True

        for x in range(len(W_Adj_Mat)):

            if (W_Adj_Mat[Closest, x, 0] and not Visited[x]):

                Distance[x]=min(Distance[x], W_Adj_Mat[Closest, x, 1])
                Neighbour[x]=Closest

        Closest=Closest_Neighbour()

    return Neighbour


def Prim_Algorithm_WAL(W_Adj_List : dict):

    WAL_Initialize(W_Adj_List)

    Closest=Closest_Neighbour()

    while(Closest is not None):

        Visited[Closest]=True

        for v, w in W_Adj_List[Closest]:

            if (not Visited[v]):

                Distance[v]=min(Distance[v], w)
                Neighbour[v]=Closest

        Closest=Closest_Neighbour()

    return Neighbour


if __name__=="__main__":

    W_Adj_List={
        
        0:[(1, 10), (2, 80)],
        1:[(0, 10), (2, 6), (4, 20)],
        2:[(0, 80), (1, 6), (3, 70)],
        3:[(2, 70)],
        4:[(1, 20), (5, 50), (6, 5)],
        5:[(4, 50), (6, 10)],
        6:[(4, 5), (5, 10)]

    }

    num_vertices = len(W_Adj_List)

    W_Adj_Mat = np.zeros((num_vertices, num_vertices, 2), dtype=int)

    for vertex, neighbors in W_Adj_List.items():
        for neighbor, weight in neighbors:
            W_Adj_Mat[vertex, neighbor, 0] = 1
            W_Adj_Mat[vertex, neighbor, 1] = weight

    Prim_Algorithm_WAM(W_Adj_Mat)
    print(Neighbour, Distance)

    Prim_Algorithm_WAL(W_Adj_List)
    print(Neighbour)