import numpy as np

Distance = {}

def WAM_Initialize(W_Adj_Mat : np.array):

    (Rows, Cols, x)=W_Adj_Mat.shape

    for x in range(Rows):

        Distance[x]=float("inf")

    return


def WAL_Initialize(W_Adj_List : dict):

    for x in W_Adj_List.keys():

        Distance[x]=float("inf")

    return


def Bellman_Ford_Algorithm_WAM(W_Adj_Mat : np.array, Start : int):

    WAM_Initialize(W_Adj_Mat)

    Distance[Start]=0
    
    for x in Distance:

        for y in Distance:

            for z in Distance:

                if (W_Adj_Mat[y][z][0]):

                    Distance[z]=min(Distance[z], Distance[y]+W_Adj_Mat[y][z][1])

    return Distance


def Bellman_Ford_Algorithm_WAL(Adj_List : dict, Start : int):

    WAL_Initialize(W_Adj_List)

    Distance[Start]=0
    
    for x in W_Adj_List:

        for y in W_Adj_List:

            for z in W_Adj_List[y]:

                Distance[z[0]]=min(Distance[z[0]], Distance[y]+z[1])

    return Distance


if __name__=="__main__":

    W_Adj_List={

        0: [(1, 10), (5, 8)],
        1: [(2, 1), (3, -2)],
        2: [],
        3: [(4, -1)],
        4: [(5, -1)],
        5: [(6, -1)],
        6: [(0, 8)]

    }

    num_vertices = len(W_Adj_List)

    W_Adj_Mat = np.zeros((num_vertices, num_vertices, 2), dtype=int)

    for vertex, neighbors in W_Adj_List.items():
        for neighbor, weight in neighbors:
            W_Adj_Mat[vertex, neighbor, 0] = 1
            W_Adj_Mat[vertex, neighbor, 1] = weight

    Bellman_Ford_Algorithm_WAM(W_Adj_Mat, 0)
    print(Distance)

    Bellman_Ford_Algorithm_WAL(W_Adj_List, 0)
    print(Distance)