import numpy as np

def Initialize(W_Adj_Mat : np.array):

    (Rows, Cols, x)=W_Adj_Mat.shape

    Shortest_Path=np.full((Rows, Cols, Cols+1), float("inf"))

    for x in range(Rows):

       for y in range(Cols):

        if (W_Adj_Mat[x, y, 0]):

            Shortest_Path[x, y, 0]=W_Adj_Mat[x, y, 1]

    return Shortest_Path


def Floyd_Warshall_Algorithm(W_Adj_Mat : np.array):

    Shortest_Path=Initialize(W_Adj_Mat)

    Len=len(Shortest_Path)

    for z in range(1, Len+1):

        for x in range(Len):

            for y in range(Len):

                Shortest_Path[x, y, z]=min(Shortest_Path[x, y, z-1], Shortest_Path[x, z-1, z-1]+Shortest_Path[z-1, y, z-1])

    return Shortest_Path[:, :, Len]


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

    print(Floyd_Warshall_Algorithm(W_Adj_Mat))